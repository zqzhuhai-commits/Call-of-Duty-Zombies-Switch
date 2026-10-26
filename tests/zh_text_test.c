#include <assert.h>
#include <stdio.h>
#include "source/zh_text.h"
int main(void) {
 const char *p="中文A";
 assert(ZH_Decode(&p)==0x4e2d); assert(ZH_Decode(&p)==0x6587);
 assert(ZH_Decode(&p)=='A'); assert(ZH_Decode(&p)==0);
 const char *bad="\xe4\xb8"; assert(ZH_Decode(&bad)==0xe4);
 assert(ZH_Decode(&bad)==0xb8);assert(!*bad);
 const char *overlong="\xe0\x80\x80";assert(ZH_Decode(&overlong)==0xe0);
 const char *emoji="\xf0\x9f\x98\x80";assert(ZH_Decode(&emoji)==0x1f600);
 assert(ZH_GlyphIndex(0x4e2d)>=0);assert(ZH_GlyphIndex(0x1f600)==-1);
 assert(!strcmp(ZH_Translate("MAIN MENU"),"主菜单"));
 assert(!strcmp(ZH_Translate("sv_maxai"),"sv_maxai"));
 for(size_t i=0;i<sizeof(zh_catalog)/sizeof(zh_catalog[0]);++i){
  assert(!strcmp(ZH_Translate(zh_catalog[i].en),zh_catalog[i].zh));
  const char *s=zh_catalog[i].zh;
  while(*s){unsigned cp=ZH_Decode(&s);assert(cp<=255||ZH_GlyphIndex(cp)>=0);}
 }
 puts("PASS: UTF-8 validation, translation lookup, complete catalog glyph coverage");
}
