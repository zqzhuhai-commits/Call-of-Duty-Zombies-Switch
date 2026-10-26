#include <switch.h>
#include <stdio.h>
#include <stdbool.h>

#ifdef PROBE_EARLY
#define LOG_PATH "sdmc:/nzp-probe-b.log"
static bool sm_ok, fs_ok, mounted, am_ok;
static Result am_result;
#else
#define LOG_PATH "sdmc:/nzp-probe-a.log"
#endif
static void mark(const char *stage, unsigned int rc) {
    FILE *f = fopen(LOG_PATH, "a");
    if (f) { fprintf(f, "%s: 0x%08x\n", stage, rc); fclose(f); }
}
static void begin_log(void) {
    FILE *f = fopen(LOG_PATH, "w");
    if (f) { fprintf(f, "NZP native probe %s\n", envIsNso() ? "NSO" : "NRO"); fclose(f); }
}
#ifdef PROBE_EARLY
/* Mount SD before the application service, so its result can be recorded. */
void __appInit(void) {
    Result rc = smInitialize(); sm_ok = R_SUCCEEDED(rc);
    if (!sm_ok) return;
    if (hosversionGet() == 0 && R_SUCCEEDED(setsysInitialize())) {
        SetSysFirmwareVersion fw;
        if (R_SUCCEEDED(setsysGetFirmwareVersion(&fw)))
            hosversionSet(MAKEHOSVERSION(fw.major, fw.minor, fw.micro));
        setsysExit();
    }
    rc = fsInitialize(); fs_ok = R_SUCCEEDED(rc);
    if (!fs_ok) return;
    int sd = fsdevMountSdmc(); mounted = sd == 0;
    if (!mounted) return;
    begin_log();
    mark("service manager and filesystem ready", 0);
    mark("firmware", hosversionGet());
    mark("appletInitialize entered", 0);
    am_result = appletInitialize(); am_ok = R_SUCCEEDED(am_result);
    mark("appletInitialize returned", am_result);
}
void __appExit(void) {
    mark("probe cleanup entered", 0);
    if (fs_ok) { fsdevUnmountAll(); fsExit(); }
    if (am_ok) appletExit();
    if (sm_ok) smExit();
}
#else
void userAppInit(void) { begin_log(); mark("standard libnx initialization completed", 0); }
#endif
int main(void) {
    mark("main entered", 0);
#ifdef PROBE_EARLY
    mark("black-screen ten-second timer entered", 0);
    svcSleepThread(10000000000LL);
    mark("timer completed; returning HOME", 0);
#else
    mark("consoleInit entered", 0);
    consoleInit(NULL);
    mark("consoleInit completed", 0);
    printf("NZP NATIVE PROBE A\n\nNSO main reached.\nStandard libnx initialization passed.\n\nPress PLUS to return HOME.\nLog: SD:/nzp-probe-a.log\n");
    PadState pad;
    padConfigureInput(1, HidNpadStyleSet_NpadStandard);
    padInitializeDefault(&pad);
    u64 start = armGetSystemTick();
    while (appletMainLoop() && armTicksToNs(armGetSystemTick()-start) < 45000000000ULL) {
        padUpdate(&pad);
        if (padGetButtonsDown(&pad) & HidNpadButton_Plus) break;
        consoleUpdate(NULL);
    }
    mark("probe A exit", 0);
    consoleExit(NULL);
#endif
    return 0;
}
