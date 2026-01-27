#!/usr/bin/env python3
"""Format ZMK keymap layers as 14x4 grids."""

def format_layer(name, label, grid):
    """Format layer from 14x4 grid. Col 6 gets +6 padding, others +2."""
    col_widths = [max(len(grid[r][c]) for r in range(4)) for c in range(14)]

    def fmt_row(row_idx):
        parts = []
        for col in range(14):
            key = grid[row_idx][col]
            w = col_widths[col]
            pad = 6 if col == 6 else 2
            if col == 13:
                parts.append(key)
            else:
                parts.append(f"{key:<{w + pad}}")
        return "".join(parts).rstrip()

    return "\n".join([
        f"                {name} {{",
        f'label= "{label}";',
        "bindings = <",
        fmt_row(0),
        fmt_row(1),
        fmt_row(2),
        fmt_row(3),
        ">;",
        "                };"
    ])

# Layers as (name, label, 14x4 grid)
# Grid columns: 0=outer_l, 1-5=left, 6=thumb_l3, 7=thumb_r1, 8-12=right, 13=outer_r
layers = [
    ("colemak_pc_layer", "COLEMAK PC", [
        ["",          "&kp Q", "&kp W", "&kp F", "&kp P",   "&kp B",   "",        "",        "&kp J",   "&kp L", "&kp U",     "&kp Y",   "&kp SQT", ""],
        ["&kp LSHFT", "hm_a",  "hm_r",  "hm_s",  "hm_t",    "&kp G",   "",        "",        "&kp M",   "hm_n",  "hm_e",      "hm_i",    "hm_o",    "mo_bt"],
        ["",          "&kp Z", "&kp X", "&kp C", "&kp D",   "&kp V",   "",        "",        "&kp K",   "&kp H", "&kp COMMA", "&kp DOT", "&kp FSLH", ""],
        ["",          "",      "",      "",      "&pcl_sh", "&pcl_br", "&pcl_na", "&pcl_nu", "&pcl_sy", "&pcl_fn", "",        "",        "",        ""],
    ]),
    ("colemak_mac_layer", "COLEMAK MAC", [
        ["",          "&kp Q", "&kp W", "&kp F", "&kp P",   "&kp B",   "",        "",        "&kp J",   "&kp L", "&kp U",     "&kp Y",   "&kp SQT", ""],
        ["&kp LSHFT", "hm_a",  "hm_r",  "hm_s",  "hm_t",    "&kp G",   "",        "",        "&kp M",   "hm_n",  "hm_e",      "hm_i",    "hm_o",    "mo_bt"],
        ["",          "&kp Z", "&kp X", "&kp C", "&kp D",   "&kp V",   "",        "",        "&kp K",   "&kp H", "&kp COMMA", "&kp DOT", "&kp FSLH", ""],
        ["",          "",      "",      "",      "&mcl_sh", "&mcl_br", "&mcl_na", "&mcl_nu", "&mcl_sy", "&mcl_fn", "",        "",        "",        ""],
    ]),
    ("qwerty_gaming_layer", "QWERTY GAMING", [
        ["",         "&kp Q", "&kp W", "&kp E", "&kp R",   "&kp T",     "",        "",        "&kp Y",   "&kp U",    "&kp I",     "&kp O",   "&kp P",    ""],
        ["&kp LGUI", "&kp A", "&kp S", "&kp D", "&kp F",   "&kp G",     "",        "",        "&kp H",   "&kp J",    "&kp K",     "&kp L",   "&kp SEMI", "mo_bt"],
        ["",         "&kp Z", "&kp X", "&kp C", "&kp V",   "&kp B",     "",        "",        "&kp N",   "&kp M",    "&kp COMMA", "&kp DOT", "&kp FSLH", ""],
        ["",         "",      "",      "",      "&kp ESC", "&kp SPACE", "&kp TAB", "&kp RET", "&kp BSPC", "&kp DEL", "",          "",        "",         ""],
    ]),
    ("symbols_layer", "SYMBOLS", [
        ["",       "&k_at",   "&k_dllr", "&k_hash", "&k_pcnt", "&k_star", "",      "",      "&k_star", "&k_pcnt", "&k_hash", "&k_dllr", "&k_at",   ""],
        ["&trans", "&k_ampr", "&k_pipe", "&k_cart", "&kp BSLH", "&kp FSLH", "",   "",      "&kp FSLH", "&kp BSLH", "&k_cart", "&k_pipe", "&k_ampr", "&trans"],
        ["",       "&k_tild", "&k_plus", "&kp MINUS", "&k_undr", "&k_ques", "",   "",      "&k_ques", "&k_undr", "&kp MINUS", "&k_plus", "&k_tild", ""],
        ["",       "",        "",        "",        "&none",   "&none",   "&none", "&none", "&none",   "&none",   "",        "",        "",        ""],
    ]),
    ("brackets_pc_layer", "BRACKETS PC", [
        ["",       "&kp LBKT", "&kp RBKT", "&k_lt",   "&k_gt",   "&k_coln", "",      "",      "&k_coln", "&k_lt",   "&k_gt",   "&kp LBKT", "&kp RBKT", ""],
        ["&trans", "&k_lcrl",  "&k_rcrl",  "&k_lprn", "&k_rprn", "&kp SEMI", "",     "",      "&kp SEMI", "&k_lprn", "&k_rprn", "&k_lcrl",  "&k_rcrl",  "&trans"],
        ["",       "&kp GRAVE", "&kp SQT", "&k_dquo", "&k_excl", "&kp EQUAL", "",    "",      "&kp EQUAL", "&k_excl", "&k_dquo", "&kp SQT", "&kp GRAVE", ""],
        ["",       "",         "",        "",        "&none",   "&none",   "&none", "&none", "&pc_dlwd", "&pc_dlwf", "",        "",        "",         ""],
    ]),
    ("brackets_mac_layer", "BRACKETS MAC", [
        ["",       "&kp LBKT", "&kp RBKT", "&k_lt",   "&k_gt",   "&k_coln", "",      "",      "&k_coln", "&k_lt",   "&k_gt",   "&kp LBKT", "&kp RBKT", ""],
        ["&trans", "&k_lcrl",  "&k_rcrl",  "&k_lprn", "&k_rprn", "&kp SEMI", "",     "",      "&kp SEMI", "&k_lprn", "&k_rprn", "&k_lcrl",  "&k_rcrl",  "&trans"],
        ["",       "&kp GRAVE", "&kp SQT", "&k_dquo", "&k_excl", "&kp EQUAL", "",    "",      "&kp EQUAL", "&k_excl", "&k_dquo", "&kp SQT", "&kp GRAVE", ""],
        ["",       "",         "",        "",        "&none",   "&none",   "&none", "&none", "&mc_dlwd", "&mc_dlwf", "",        "",        "",         ""],
    ]),
    ("numbers_layer", "NUMBERS", [
        ["",       "&k_star",   "&kp N7", "&kp N8", "&kp N9", "&k_plus",    "",        "",      "&k_plus",    "&kp N7",    "&kp N8", "&kp N9", "&k_star",   ""],
        ["&trans", "&kp FSLH",  "&kp N4", "&kp N5", "&kp N6", "&kp MINUS",  "",        "",      "&kp MINUS",  "&kp N4",    "&kp N5", "&kp N6", "&kp FSLH",  "&trans"],
        ["",       "&kp N0",    "&kp N1", "&kp N2", "&kp N3", "&kp EQUAL",  "",        "",      "&kp EQUAL",  "&kp N1",    "&kp N2", "&kp N3", "&kp N0",    ""],
        ["",       "",          "",       "",       "&kp COMMA", "&kp DOT", "&kp RET", "&none", "&kp DOT",    "&kp COMMA", "",       "",       "",          ""],
    ]),
    ("navigation_pc_layer", "NAVIGATION PC", [
        ["",       "&pc_undo",  "&pc_cut",  "&pc_copy", "&pc_pste", "&pc_redo", "",      "",      "&pc_redo", "&pc_pste", "&pc_copy", "&pc_cut",  "&pc_undo", ""],
        ["&trans", "&kp HOME",  "&kp PG_DN", "&kp PG_UP", "&kp END", "&pc_prnt", "",     "",      "&pc_prnt", "&kp LEFT", "&kp DOWN", "&kp UP",   "&kp RIGHT", "&trans"],
        ["",       "&pc_gtln",  "&pc_zmbk", "&pc_zmfw", "&pc_swfl", "&pc_palt", "",      "",      "&pc_palt", "&pc_swfl", "&pc_zmfw", "&pc_zmbk", "&pc_gtln", ""],
        ["",       "",          "",         "",         "&pc_slal", "&pc_save", "&none", "&none", "&kp BSPC", "&kp DEL",  "",         "",         "",         ""],
    ]),
    ("navigation_mac_layer", "NAVIGATION MAC", [
        ["",       "&mc_undo",  "&mc_cut",  "&mc_copy", "&mc_pste", "&mc_redo", "",      "",      "&mc_redo", "&mc_pste", "&mc_copy", "&mc_cut",  "&mc_undo", ""],
        ["&trans", "&kp HOME",  "&kp PG_DN", "&kp PG_UP", "&kp END", "&mc_prnt", "",     "",      "&mc_prnt", "&kp LEFT", "&kp DOWN", "&kp UP",   "&kp RIGHT", "&trans"],
        ["",       "&mc_gtln",  "&mc_zmbk", "&mc_zmfw", "&mc_swfl", "&mc_palt", "",      "",      "&mc_palt", "&mc_swfl", "&mc_zmfw", "&mc_zmbk", "&mc_gtln", ""],
        ["",       "",          "",         "",         "&mc_slal", "&mc_save", "&none", "&none", "&kp BSPC", "&kp DEL",  "",         "",         "",         ""],
    ]),
    ("shortcuts_pc_layer", "SHORTCUTS PC", [
        ["",      "&pc_scrn", "&pc_cmnt", "&pc_rpfl", "&pc_fnfl", "&pc_zmin", "",       "",       "&pc_zmin", "&pc_fnfl", "&pc_rpfl", "&pc_cmnt", "&pc_scrn", ""],
        ["&trans", "&pc_shot", "&pc_frmt", "&pc_rplc", "&pc_find", "&pc_zmot", "",       "",       "&pc_zmot", "&pc_find", "&pc_rplc", "&pc_frmt", "&pc_shot", "&trans"],
        ["",      "&pc_srec", "&pc_gdef", "&pc_gimp", "&pc_qfix", "&pc_ctab", "",       "",       "&pc_ctab", "&pc_qfix", "&pc_gimp", "&pc_gdef", "&pc_srec", ""],
        ["",      "",         "",         "",         "&trans",   "&trans",   "&trans", "&trans", "&trans",   "&trans",   "",         "",         "",         ""],
    ]),
    ("shortcuts_mac_layer", "SHORTCUTS MAC", [
        ["",      "&mc_scrn", "&mc_cmnt", "&mc_rpfl", "&mc_fnfl", "&mc_zmin", "",       "",       "&mc_zmin", "&mc_fnfl", "&mc_rpfl", "&mc_cmnt", "&mc_scrn", ""],
        ["&trans", "&mc_shot", "&mc_frmt", "&mc_rplc", "&mc_find", "&mc_zmot", "",       "",       "&mc_zmot", "&mc_find", "&mc_rplc", "&mc_frmt", "&mc_shot", "&trans"],
        ["",      "&mc_srec", "&mc_gdef", "&mc_gimp", "&mc_qfix", "&mc_ctab", "",       "",       "&mc_ctab", "&mc_qfix", "&mc_gimp", "&mc_gdef", "&mc_srec", ""],
        ["",      "",         "",         "",         "&trans",   "&trans",   "&trans", "&trans", "&trans",   "&trans",   "",         "",         "",         ""],
    ]),
    ("function_layer", "FUNCTION", [
        ["",      "to_pc",   "&kp F9", "&kp F8", "&kp F7", "&kp F10", "",      "",      "&kp F10", "&kp F7", "&kp F8", "&kp F9", "to_pc",   ""],
        ["&trans", "to_mac",  "&kp F6", "&kp F5", "&kp F4", "&kp F11", "",      "",      "&kp F11", "&kp F4", "&kp F5", "&kp F6", "to_mac",  "&trans"],
        ["",      "to_game", "&kp F3", "&kp F2", "&kp F1", "&kp F12", "",      "",      "&kp F12", "&kp F1", "&kp F2", "&kp F3", "to_game", ""],
        ["",      "",        "",       "",       "&none",  "&none",   "&none", "&none", "&none",   "&none",  "",       "",       "",        ""],
    ]),
    ("bluetooth_layer", "BLUETOOTH", [
        ["",       "&bt0_pc",    "&bt1_mac",     "&bt2",       "&bt3",        "&bt4",   "",       "",       "&trans", "&trans", "&trans", "&trans", "to_pc",   ""],
        ["&trans", "&trans",     "&trans",       "&trans",     "&trans",      "&trans", "",       "",       "&trans", "&trans", "&trans", "&trans", "to_mac",  "&trans"],
        ["",       "&bt BT_CLR", "&out OUT_TOG", "&sys_reset", "&bootloader", "&trans", "",       "",       "&trans", "&trans", "&trans", "&trans", "to_game", ""],
        ["",       "",           "",             "",           "&trans",      "&trans", "&trans", "&trans", "&trans", "&trans", "",       "",       "",        ""],
    ]),
]

header = """#include <behaviors.dtsi>
#include <dt-bindings/zmk/keys.h>
#include <dt-bindings/zmk/bt.h>
#include <dt-bindings/zmk/outputs.h>

#define COLEMAK_PC 0
#define COLEMAK_MAC 1
#define QWERTY_GAMING 2
#define SYMBOLS 3
#define BRACKETS_PC 4
#define BRACKETS_MAC 5
#define NUMBERS 6
#define NAVIGATION_PC 7
#define NAVIGATION_MAC 8
#define SHORTCUTS_PC 9
#define SHORTCUTS_MAC 10
#define FUNCTION 11
#define BLUETOOTH 12

// Home row mods
#define hm_a &mt LGUI A
#define hm_r &mt LALT R
#define hm_s &mt LCTRL S
#define hm_t &mt LSHFT T
#define hm_n &mt RSHFT N
#define hm_e &mt RCTRL E
#define hm_i &mt RALT I
#define hm_o &mt RGUI O

// Layer switches
#define to_pc &to COLEMAK_PC
#define to_mac &to COLEMAK_MAC
#define to_game &to QWERTY_GAMING
#define mo_bt &mo BLUETOOTH

&mt {
  quick-tap-ms = <100>;
  global-quick-tap;
  flavor = "tap-preferred";
  tapping-term-ms = <170>;
};

/ {
        macros {
                // BT profile macros
                bt0_pc: bt0_pc {
                        compatible = "zmk,behavior-macro";
                        #binding-cells = <0>;
                        bindings = <&bt BT_SEL 0>, <&to COLEMAK_PC>;
                };
                bt1_mac: bt1_mac {
                        compatible = "zmk,behavior-macro";
                        #binding-cells = <0>;
                        bindings = <&bt BT_SEL 1>, <&to COLEMAK_MAC>;
                };
                bt2: bt2 { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&bt BT_SEL 2>; };
                bt3: bt3 { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&bt BT_SEL 3>; };
                bt4: bt4 { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&bt BT_SEL 4>; };

                // PC Layer-tap macros
                pcl_sh: pcl_sh { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&lt SHORTCUTS_PC ESC>; };
                pcl_br: pcl_br { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&lt BRACKETS_PC SPACE>; };
                pcl_na: pcl_na { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&lt NAVIGATION_PC TAB>; };
                pcl_nu: pcl_nu { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&lt NUMBERS RET>; };
                pcl_sy: pcl_sy { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&lt SYMBOLS BSPC>; };
                pcl_fn: pcl_fn { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&lt FUNCTION DEL>; };

                // Mac Layer-tap macros
                mcl_sh: mcl_sh { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&lt SHORTCUTS_MAC ESC>; };
                mcl_br: mcl_br { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&lt BRACKETS_MAC SPACE>; };
                mcl_na: mcl_na { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&lt NAVIGATION_MAC TAB>; };
                mcl_nu: mcl_nu { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&lt NUMBERS RET>; };
                mcl_sy: mcl_sy { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&lt SYMBOLS BSPC>; };
                mcl_fn: mcl_fn { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&lt FUNCTION DEL>; };

                // PC Shortcuts
                pc_scrn: pc_scrn { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp PSCRN>; };
                pc_cmnt: pc_cmnt { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(FSLH)>; };
                pc_rpfl: pc_rpfl { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(LS(H))>; };
                pc_fnfl: pc_fnfl { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(LS(F))>; };
                pc_zmin: pc_zmin { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(LS(EQUAL))>; };
                pc_zmot: pc_zmot { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(MINUS)>; };
                pc_shot: pc_shot { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(LS(S))>; };
                pc_frmt: pc_frmt { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(LA(F))>; };
                pc_rplc: pc_rplc { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(H)>; };
                pc_find: pc_find { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(F)>; };
                pc_srec: pc_srec { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(LA(R))>; };
                pc_gdef: pc_gdef { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp F12>; };
                pc_gimp: pc_gimp { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(F12)>; };
                pc_qfix: pc_qfix { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(DOT)>; };
                pc_ctab: pc_ctab { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(W)>; };
                pc_capp: pc_capp { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(F4)>; };

                // Mac Shortcuts
                mc_scrn: mc_scrn { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(LS(N3))>; };
                mc_cmnt: mc_cmnt { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(FSLH)>; };
                mc_rpfl: mc_rpfl { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(LS(H))>; };
                mc_fnfl: mc_fnfl { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(LS(F))>; };
                mc_zmin: mc_zmin { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(LS(EQUAL))>; };
                mc_zmot: mc_zmot { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(MINUS)>; };
                mc_shot: mc_shot { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(LS(N4))>; };
                mc_frmt: mc_frmt { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(LA(F))>; };
                mc_rplc: mc_rplc { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(LA(F))>; };
                mc_find: mc_find { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(F)>; };
                mc_srec: mc_srec { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(LS(N5))>; };
                mc_gdef: mc_gdef { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp F12>; };
                mc_gimp: mc_gimp { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(F12)>; };
                mc_qfix: mc_qfix { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(DOT)>; };
                mc_ctab: mc_ctab { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(W)>; };
                mc_capp: mc_capp { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(Q)>; };

                // Shifted number symbols: ! @ # $ % ^ & * ( )
                k_excl: k_excl { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(N1)>; };
                k_at:   k_at   { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(N2)>; };
                k_hash: k_hash { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(N3)>; };
                k_dllr: k_dllr { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(N4)>; };
                k_pcnt: k_pcnt { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(N5)>; };
                k_cart: k_cart { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(N6)>; };
                k_ampr: k_ampr { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(N7)>; };
                k_star: k_star { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(N8)>; };
                k_lprn: k_lprn { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(N9)>; };
                k_rprn: k_rprn { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(N0)>; };

                // Shifted punctuation
                k_pipe: k_pipe { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(BSLH)>; };
                k_plus: k_plus { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(EQUAL)>; };
                k_undr: k_undr { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(MINUS)>; };
                k_tild: k_tild { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(GRAVE)>; };
                k_lcrl: k_lcrl { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(LBKT)>; };
                k_rcrl: k_rcrl { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(RBKT)>; };
                k_lt:   k_lt   { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(COMMA)>; };
                k_gt:   k_gt   { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(DOT)>; };
                k_coln: k_coln { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(SEMI)>; };
                k_dquo: k_dquo { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(SQT)>; };
                k_ques: k_ques { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LS(FSLH)>; };

                // PC Navigation combos
                pc_undo: pc_undo { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(Z)>; };
                pc_redo: pc_redo { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(LS(Z))>; };
                pc_cut:  pc_cut  { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(X)>; };
                pc_copy: pc_copy { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(C)>; };
                pc_pste: pc_pste { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(V)>; };
                pc_slal: pc_slal { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(A)>; };
                pc_save: pc_save { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(S)>; };
                pc_gtln: pc_gtln { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(G)>; };
                pc_zmbk: pc_zmbk { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(MINUS)>; };
                pc_zmfw: pc_zmfw { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(LS(MINUS))>; };
                pc_swfl: pc_swfl { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(LS(O))>; };
                pc_prnt: pc_prnt { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(P)>; };
                pc_palt: pc_palt { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(LS(P))>; };

                // Mac Navigation combos
                mc_undo: mc_undo { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(Z)>; };
                mc_redo: mc_redo { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(LS(Z))>; };
                mc_cut:  mc_cut  { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(X)>; };
                mc_copy: mc_copy { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(C)>; };
                mc_pste: mc_pste { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(V)>; };
                mc_slal: mc_slal { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(A)>; };
                mc_save: mc_save { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(S)>; };
                mc_gtln: mc_gtln { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(G)>; };
                mc_zmbk: mc_zmbk { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(MINUS)>; };
                mc_zmfw: mc_zmfw { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(LS(MINUS))>; };
                mc_swfl: mc_swfl { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(LS(O))>; };
                mc_prnt: mc_prnt { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(P)>; };
                mc_palt: mc_palt { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LG(LS(P))>; };

                // Delete word macros
                pc_dlwd: pc_dlwd { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(BSPC)>; };
                pc_dlwf: pc_dlwf { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LC(DEL)>; };
                mc_dlwd: mc_dlwd { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LA(BSPC)>; };
                mc_dlwf: mc_dlwf { compatible = "zmk,behavior-macro"; #binding-cells = <0>; bindings = <&kp LA(DEL)>; };
        };

        keymap {
                compatible = "zmk,keymap";
"""

footer = """        };
};
"""

if __name__ == "__main__":
    output = header
    for name, label, grid in layers:
        output += "\n" + format_layer(name, label, grid) + "\n"
    output += footer

    with open("config/totem.keymap", "w") as f:
        f.write(output)

    print("Generated config/totem.keymap")
    print("\nPreview of first layer:")
    print(format_layer(layers[0][0], layers[0][1], layers[0][2]))
