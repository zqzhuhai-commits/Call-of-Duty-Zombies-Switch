/* Simplified Chinese support. GPL-2.0-or-later, matching the engine. */
#ifndef NZP_ZH_TEXT_H
#define NZP_ZH_TEXT_H
#include <stddef.h>
#include <string.h>
#include "zh_catalog.h"
/* Translate display text only. Commands, resource names and cvars stay intact. */
static const char *ZH_Translate(const char *text)
{
    size_t lo = 0, hi = sizeof(zh_catalog) / sizeof(zh_catalog[0]);
    if (!text) return "";
    while (lo < hi) {
        size_t mid = lo + (hi - lo) / 2;
        int cmp = strcmp(text, zh_catalog[mid].en);
        if (!cmp) return zh_catalog[mid].zh;
        if (cmp < 0) hi = mid; else lo = mid + 1;
    }
    return text;
}
/* Strict UTF-8. Invalid legacy bytes consume one byte and retain Quake glyphs. */
static unsigned int ZH_Decode(const char **cursor)
{
    const unsigned char *s = (const unsigned char *)*cursor;
    unsigned int cp; int n, i;
    if (s[0] < 0x80) { if (s[0]) ++*cursor; return s[0]; }
    if (s[0] >= 0xc2 && s[0] <= 0xdf) { cp=s[0]&31; n=2; }
    else if (s[0] >= 0xe0 && s[0] <= 0xef) { cp=s[0]&15; n=3; }
    else if (s[0] >= 0xf0 && s[0] <= 0xf4) { cp=s[0]&7; n=4; }
    else { ++*cursor; return s[0]; }
    for (i=1; i<n; ++i) {
        if (!s[i] || (s[i]&0xc0)!=0x80) { ++*cursor; return s[0]; }
        cp=(cp<<6)|(s[i]&63);
    }
    if ((n==3 && cp<0x800) || (n==4 && cp<0x10000) ||
        (cp>=0xd800 && cp<=0xdfff) || cp>0x10ffff) { ++*cursor; return s[0]; }
    *cursor += n; return cp;
}
static int ZH_GlyphIndex(unsigned int cp)
{
    int lo=0, hi=ZH_GLYPH_COUNT;
    while(lo<hi) { int m=lo+(hi-lo)/2;
        if (zh_codepoints[m]==cp) return m;
        if (cp<zh_codepoints[m]) hi=m; else lo=m+1;
    }
    return -1;
}
#endif
