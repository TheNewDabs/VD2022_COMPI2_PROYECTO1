/*----HEADER----*/
package main;

import (
	"fmt"
	"math"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39, t40, t41, t42, t43, t44, t45, t46, t47, t48, t49, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59, t60, t61, t62, t63, t64, t65, t66, t67, t68, t69, t70, t71, t72, t73, t74, t75, t76, t77, t78, t79, t80, t81, t82, t83, t84, t85, t86, t87, t88, t89, t90, t91, t92, t93, t94, t95, t96, t97, t98, t99, t100, t101, t102, t103, t104, t105, t106, t107, t108, t109, t110, t111, t112, t113, t114, t115, t116, t117, t118, t119, t120, t121, t122, t123, t124, t125, t126, t127, t128, t129, t130, t131, t132, t133, t134, t135, t136, t137, t138, t139, t140, t141, t142, t143, t144, t145, t146, t147, t148, t149, t150, t151, t152, t153, t154, t155, t156, t157, t158, t159, t160, t161, t162, t163, t164, t165, t166, t167, t168, t169, t170, t171, t172, t173, t174, t175, t176, t177, t178, t179, t180, t181, t182, t183, t184, t185, t186, t187, t188, t189, t190, t191, t192, t193, t194, t195, t196, t197, t198, t199, t200, t201, t202, t203, t204, t205, t206, t207, t208, t209, t210, t211, t212, t213, t214, t215, t216, t217, t218, t219, t220, t221, t222, t223, t224, t225, t226, t227, t228, t229, t230, t231, t232, t233, t234, t235, t236, t237, t238, t239 float64;
var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;

/*-----NATIVES-----*/
func print_string(){
	t48=P+1;
	t49=stack[int(t48)];
	L18:
	t50=heap[int(t49)];
	if t50 == -1 {goto L17;}
	fmt.Printf("%c", int(t50));
	t49=t49+1;
	goto L18;
	L17:
	return;
}
func print_array(){
	t196=P+1;
	t197=stack[int(t196)];
	t199=heap[int(t197)];
	t197=t197+1;
	fmt.Printf("%c", int(91));
	L70:
	t201=heap[int(t197)];
	t200=t201;
	if t198 >= t199 {goto L69;}
	if t19 == t200 {goto L72;}
	if t21 == t200 {goto L72;}
	if t24 == t200 {goto L72;}
	if t40 == t200 {goto L72;}
	if t43 == t200 {goto L72;}
	if t45 == t200 {goto L72;}
	fmt.Printf("%f", t201);
	fmt.Printf("%c", int(44));
	t197=t197+1;
	t198=t198+1;
	goto L70;
	L72:
	t202=P;
	t203=t198;
	t204=t199;
	t205=t201;
	t206=t196;
	t207=t197;
	t198=0;
	stack[int(t196)]=t201;
	print_array();
	t198=t203+1;
	t199=t204;
	t201=t205;
	t196=t206;
	t197=t207+1;
	goto L70;
	L69:
	fmt.Printf("%c", int(93));
	t198=0;
	return;
}

/*-----FUNCS-----*/
func printMatriz(){
	t47=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=91;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t47=t47+0.12837;
	t51=P+2;
	t51=t51+1;
	stack[int(t51)]=t47;
	P=P+2;
	print_string();
	t52=stack[int(P)];
	P=P-2;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	/* compilacion length */
	/* compilacion de accesso */
	t54=P+1;
	t53=stack[int(t54)];
	/* fin de la compilacion de acceso */
	
	t55=t53;
	t55=heap[int(t55)];
	t56=1;
	L19:
	if t56 > t55 {goto L20;}
	/* compilacion de valor de variable */
	/* fin de compilacion de variable */
	t57=P+2;
	stack[int(t57)]=t56;
	
	t56=t56+1;
	t58=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=91;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t58=t58+0.12837;
	t59=P+3;
	t59=t59+1;
	stack[int(t59)]=t58;
	P=P+3;
	print_string();
	t60=stack[int(P)];
	P=P-3;
	fmt.Printf("%c", int(32));
	/* compilacion length */
	/* compilacion de acceso arreglos */
	t62=P+1;
	t61=stack[int(t62)];
	/* compilacion de accesso */
	t64=P+2;
	t63=stack[int(t64)];
	/* fin de la compilacion de acceso */
	
	t66=heap[int(t61)];
	t65=t63+t61;
	if t66 < t63 {goto L21;}
	goto L22;
	L21:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L22:
	t61=heap[int(t65)];
	t67=t61;
	t67=heap[int(t67)];
	t68=1;
	L23:
	if t68 > t67 {goto L24;}
	/* compilacion de valor de variable */
	/* fin de compilacion de variable */
	t69=P+3;
	stack[int(t69)]=t68;
	
	t68=t68+1;
	/* compilacion de acceso arreglos */
	t71=P+1;
	t70=stack[int(t71)];
	/* compilacion de accesso */
	t73=P+2;
	t72=stack[int(t73)];
	/* fin de la compilacion de acceso */
	
	t75=heap[int(t70)];
	t74=t72+t70;
	if t75 < t72 {goto L25;}
	goto L26;
	L25:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L26:
	t70=heap[int(t74)];
	/* compilacion de accesso */
	t77=P+3;
	t76=stack[int(t77)];
	/* fin de la compilacion de acceso */
	
	t79=heap[int(t70)];
	t78=t76+t70;
	if t79 < t76 {goto L27;}
	goto L28;
	L27:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L28:
	t70=heap[int(t78)];
	fmt.Printf("%d", int(t70));
	fmt.Printf("%c", int(32));
	t80=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t80=t80+0.12837;
	t81=P+4;
	t81=t81+1;
	stack[int(t81)]=t80;
	P=P+4;
	print_string();
	t82=stack[int(P)];
	P=P-4;
	fmt.Printf("%c", int(32));
	/* compilacion de valor de variable */
	/* fin de compilacion de variable */
	t83=P+3;
	stack[int(t83)]=t68;
	
	goto L23;
	L24:
	t84=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=93;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t84=t84+0.12837;
	t85=P+3;
	t85=t85+1;
	stack[int(t85)]=t84;
	P=P+3;
	print_string();
	t86=stack[int(P)];
	P=P-3;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	/* compilacion de valor de variable */
	/* fin de compilacion de variable */
	t87=P+2;
	stack[int(t87)]=t56;
	
	goto L19;
	L20:
	t88=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=93;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t88=t88+0.12837;
	t89=P+2;
	t89=t89+1;
	stack[int(t89)]=t88;
	P=P+2;
	print_string();
	t90=stack[int(P)];
	P=P-2;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	return;
}
func sumarMatrices(){
	/* iniciando el if */
	/* inicio de expression realcional */
	/* compilacion length */
	/* compilacion de accesso */
	t92=P+1;
	t91=stack[int(t92)];
	/* fin de la compilacion de acceso */
	
	t93=t91;
	t93=heap[int(t93)];
	/* compilacion length */
	/* compilacion de accesso */
	t95=P+2;
	t94=stack[int(t95)];
	/* fin de la compilacion de acceso */
	
	t96=t94;
	t96=heap[int(t96)];
	if t93 != t96 {goto L30;}
	goto L31;
	/* fin de la expression relacional */
	
	L30:
	t97=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=78;
	H=H+1;
	heap[int(H)]=79;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=80;
	H=H+1;
	heap[int(H)]=85;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=68;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=78;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=85;
	H=H+1;
	heap[int(H)]=77;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=82;
	H=H+1;
	heap[int(H)]=46;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=78;
	H=H+1;
	heap[int(H)]=79;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=79;
	H=H+1;
	heap[int(H)]=78;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=68;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=76;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=77;
	H=H+1;
	heap[int(H)]=73;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=77;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=76;
	H=H+1;
	heap[int(H)]=79;
	H=H+1;
	heap[int(H)]=78;
	H=H+1;
	heap[int(H)]=71;
	H=H+1;
	heap[int(H)]=73;
	H=H+1;
	heap[int(H)]=84;
	H=H+1;
	heap[int(H)]=85;
	H=H+1;
	heap[int(H)]=68;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t97=t97+0.12837;
	stack[int(P)]=t97;
	goto L29;
	L31:
	/* compilacion length */
	/* compilacion de accesso */
	t99=P+1;
	t98=stack[int(t99)];
	/* fin de la compilacion de acceso */
	
	t100=t98;
	t100=heap[int(t100)];
	t101=1;
	L32:
	if t101 > t100 {goto L33;}
	/* compilacion de valor de variable */
	/* fin de compilacion de variable */
	t102=P+3;
	stack[int(t102)]=t101;
	
	t101=t101+1;
	/* compilacion length */
	/* compilacion de acceso arreglos */
	t104=P+1;
	t103=stack[int(t104)];
	t106=heap[int(t103)];
	t105=1+t103;
	if t106 < 1 {goto L34;}
	goto L35;
	L34:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L35:
	t103=heap[int(t105)];
	t107=t103;
	t107=heap[int(t107)];
	t108=1;
	L36:
	if t108 > t107 {goto L37;}
	/* compilacion de valor de variable */
	/* fin de compilacion de variable */
	t109=P+4;
	stack[int(t109)]=t108;
	
	t108=t108+1;
	/* compilacion de acceso arreglos */
	t111=P+1;
	t110=stack[int(t111)];
	/* compilacion de accesso */
	t113=P+3;
	t112=stack[int(t113)];
	/* fin de la compilacion de acceso */
	
	t115=heap[int(t110)];
	t114=t112+t110;
	if t115 < t112 {goto L38;}
	goto L39;
	L38:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L39:
	t110=heap[int(t114)];
	/* compilacion de accesso */
	t117=P+4;
	t116=stack[int(t117)];
	/* fin de la compilacion de acceso */
	
	t119=heap[int(t110)];
	t118=t116+t110;
	if t119 < t116 {goto L40;}
	goto L41;
	L40:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L41:
	t110=heap[int(t118)];
	/* compilacion de acceso arreglos */
	t121=P+2;
	t120=stack[int(t121)];
	/* compilacion de accesso */
	t123=P+3;
	t122=stack[int(t123)];
	/* fin de la compilacion de acceso */
	
	t125=heap[int(t120)];
	t124=t122+t120;
	if t125 < t122 {goto L42;}
	goto L43;
	L42:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L43:
	t120=heap[int(t124)];
	/* compilacion de accesso */
	t127=P+4;
	t126=stack[int(t127)];
	/* fin de la compilacion de acceso */
	
	t129=heap[int(t120)];
	t128=t126+t120;
	if t129 < t126 {goto L44;}
	goto L45;
	L44:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L45:
	t120=heap[int(t128)];
	t130=t110+t120;
	/* cambiando el valor de arreglo */
	t131=stack[int(3)];
	/* compilacion de accesso */
	t134=P+3;
	t133=stack[int(t134)];
	/* fin de la compilacion de acceso */
	
	t136=heap[int(t131)];
	t135=t133+t131;
	if t136 < t133 {goto L46;}
	goto L47;
	L46:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L47:
	t131=heap[int(t135)];
	t132=t135;
	/* compilacion de accesso */
	t138=P+4;
	t137=stack[int(t138)];
	/* fin de la compilacion de acceso */
	
	t140=heap[int(t131)];
	t139=t137+t131;
	if t140 < t137 {goto L48;}
	goto L49;
	L48:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L49:
	t131=heap[int(t139)];
	t132=t139;
	heap[int(t132)]=t130;
	/* compilacion de valor de variable */
	/* fin de compilacion de variable */
	t141=P+4;
	stack[int(t141)]=t108;
	
	goto L36;
	L37:
	/* compilacion de valor de variable */
	/* fin de compilacion de variable */
	t142=P+3;
	stack[int(t142)]=t101;
	
	goto L32;
	L33:
	/* compilacion de accesso */
	t143=stack[int(3)];
	/* fin de la compilacion de acceso */
	
	stack[int(P)]=t143;
	goto L29;
	L29:
	return;
}
func compararMatrices(){
	/* iniciando el if */
	/* inicio de expression realcional */
	/* compilacion length */
	/* compilacion de accesso */
	t145=P+1;
	t144=stack[int(t145)];
	/* fin de la compilacion de acceso */
	
	t146=t144;
	t146=heap[int(t146)];
	/* compilacion length */
	/* compilacion de accesso */
	t148=P+2;
	t147=stack[int(t148)];
	/* fin de la compilacion de acceso */
	
	t149=t147;
	t149=heap[int(t149)];
	if t146 != t149 {goto L51;}
	goto L52;
	/* fin de la expression relacional */
	
	L51:
	stack[int(P)]=0;
	goto L50;
	L52:
	/* compilacion length */
	/* compilacion de accesso */
	t151=P+1;
	t150=stack[int(t151)];
	/* fin de la compilacion de acceso */
	
	t152=t150;
	t152=heap[int(t152)];
	t153=1;
	L53:
	if t153 > t152 {goto L54;}
	/* compilacion de valor de variable */
	/* fin de compilacion de variable */
	t154=P+3;
	stack[int(t154)]=t153;
	
	t153=t153+1;
	/* compilacion length */
	/* compilacion de acceso arreglos */
	t156=P+1;
	t155=stack[int(t156)];
	t158=heap[int(t155)];
	t157=1+t155;
	if t158 < 1 {goto L55;}
	goto L56;
	L55:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L56:
	t155=heap[int(t157)];
	t159=t155;
	t159=heap[int(t159)];
	t160=1;
	L57:
	if t160 > t159 {goto L58;}
	/* compilacion de valor de variable */
	/* fin de compilacion de variable */
	t161=P+4;
	stack[int(t161)]=t160;
	
	t160=t160+1;
	/* iniciando el if */
	/* inicio de expression realcional */
	/* compilacion de acceso arreglos */
	t163=P+1;
	t162=stack[int(t163)];
	/* compilacion de accesso */
	t165=P+3;
	t164=stack[int(t165)];
	/* fin de la compilacion de acceso */
	
	t167=heap[int(t162)];
	t166=t164+t162;
	if t167 < t164 {goto L59;}
	goto L60;
	L59:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L60:
	t162=heap[int(t166)];
	/* compilacion de accesso */
	t169=P+4;
	t168=stack[int(t169)];
	/* fin de la compilacion de acceso */
	
	t171=heap[int(t162)];
	t170=t168+t162;
	if t171 < t168 {goto L61;}
	goto L62;
	L61:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L62:
	t162=heap[int(t170)];
	/* compilacion de acceso arreglos */
	t173=P+2;
	t172=stack[int(t173)];
	/* compilacion de accesso */
	t175=P+3;
	t174=stack[int(t175)];
	/* fin de la compilacion de acceso */
	
	t177=heap[int(t172)];
	t176=t174+t172;
	if t177 < t174 {goto L63;}
	goto L64;
	L63:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L64:
	t172=heap[int(t176)];
	/* compilacion de accesso */
	t179=P+4;
	t178=stack[int(t179)];
	/* fin de la compilacion de acceso */
	
	t181=heap[int(t172)];
	t180=t178+t172;
	if t181 < t178 {goto L65;}
	goto L66;
	L65:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L66:
	t172=heap[int(t180)];
	if t162 != t172 {goto L67;}
	goto L68;
	/* fin de la expression relacional */
	
	L67:
	stack[int(P)]=0;
	goto L50;
	L68:
	/* compilacion de valor de variable */
	/* fin de compilacion de variable */
	t182=P+4;
	stack[int(t182)]=t160;
	
	goto L57;
	L58:
	/* compilacion de valor de variable */
	/* fin de compilacion de variable */
	t183=P+3;
	stack[int(t183)]=t153;
	
	goto L53;
	L54:
	stack[int(P)]=1;
	goto L50;
	L50:
	return;
}

func main(){
	/* compilacion de valor de variable */
	t0=0-1;
	t1=0-55;
	t2=0-5;
	t3=H;
	heap[int(H)]=11;
	H=H+1;
	heap[int(H)]=1;
	H=H+1;
	heap[int(H)]=5;
	H=H+1;
	heap[int(H)]=8;
	H=H+1;
	heap[int(H)]=t0;
	H=H+1;
	heap[int(H)]=21;
	H=H+1;
	heap[int(H)]=42;
	H=H+1;
	heap[int(H)]=t1;
	H=H+1;
	heap[int(H)]=123;
	H=H+1;
	heap[int(H)]=t2;
	H=H+1;
	heap[int(H)]=5;
	H=H+1;
	heap[int(H)]=11;
	H=H+1;
	t3=t3+0.12837;
	/* fin de compilacion de variable */
	stack[int(0)]=t3;
	
	/* compilacion de valor de variable */
	/* compilacion de acceso arreglos */
	t4=stack[int(0)];
	t6=heap[int(t4)];
	t5=1+t4;
	if t6 < 1 {goto L0;}
	goto L1;
	L0:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L1:
	t4=heap[int(t5)];
	t7=t4*3;
	/* compilacion de acceso arreglos */
	t8=stack[int(0)];
	t10=heap[int(t8)];
	t9=4+t8;
	if t10 < 4 {goto L2;}
	goto L3;
	L2:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L3:
	t8=heap[int(t9)];
	if 2 == 0 {goto L4;}
	t12=2;
	t11=t8/t12;
	goto L5;
	L4:
	fmt.Printf("%c", int(109));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(104));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(114));
	L5:
	/* compilacion de acceso arreglos */
	t13=stack[int(0)];
	t15=heap[int(t13)];
	t14=3+t13;
	if t15 < 3 {goto L6;}
	goto L7;
	L6:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L7:
	t13=heap[int(t14)];
	t16=t13*10;
	t17 = math.Mod(t16,7);
	t18=H;
	heap[int(H)]=4;
	H=H+1;
	heap[int(H)]=t7;
	H=H+1;
	heap[int(H)]=51;
	H=H+1;
	heap[int(H)]=t11;
	H=H+1;
	heap[int(H)]=t17;
	H=H+1;
	t18=t18+0.12837;
	t19=t18;
	t20=H;
	heap[int(H)]=4;
	H=H+1;
	heap[int(H)]=1;
	H=H+1;
	heap[int(H)]=2;
	H=H+1;
	heap[int(H)]=3;
	H=H+1;
	heap[int(H)]=4;
	H=H+1;
	t20=t20+0.12837;
	t21=t20;
	t22=H;
	heap[int(H)]=2;
	H=H+1;
	heap[int(H)]=t18;
	H=H+1;
	heap[int(H)]=t20;
	H=H+1;
	t22=t22+0.12837;
	/* fin de compilacion de variable */
	stack[int(1)]=t22;
	
	/* compilacion de valor de variable */
	t23=H;
	heap[int(H)]=4;
	H=H+1;
	heap[int(H)]=1;
	H=H+1;
	heap[int(H)]=2;
	H=H+1;
	heap[int(H)]=3;
	H=H+1;
	heap[int(H)]=4;
	H=H+1;
	t23=t23+0.12837;
	t24=t23;
	/* compilacion de acceso arreglos */
	t25=stack[int(0)];
	t27=heap[int(t25)];
	t26=1+t25;
	if t27 < 1 {goto L8;}
	goto L9;
	L8:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L9:
	t25=heap[int(t26)];
	t28=t25*3;
	/* compilacion de acceso arreglos */
	t29=stack[int(0)];
	t31=heap[int(t29)];
	t30=4+t29;
	if t31 < 4 {goto L10;}
	goto L11;
	L10:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L11:
	t29=heap[int(t30)];
	if 2 == 0 {goto L12;}
	t33=2;
	t32=t29/t33;
	goto L13;
	L12:
	fmt.Printf("%c", int(109));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(104));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(114));
	L13:
	/* compilacion de acceso arreglos */
	t34=stack[int(0)];
	t36=heap[int(t34)];
	t35=3+t34;
	if t36 < 3 {goto L14;}
	goto L15;
	L14:
	fmt.Printf("%c", int(105));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(100));
	fmt.Printf("%c", int(101));
	fmt.Printf("%c", int(120));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(111));
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(110));
	fmt.Printf("%c", int(103));
	fmt.Printf("%c", int(101));
	return;	L15:
	t34=heap[int(t35)];
	t37=t34*10;
	t38 = math.Mod(t37,7);
	t39=H;
	heap[int(H)]=4;
	H=H+1;
	heap[int(H)]=t28;
	H=H+1;
	heap[int(H)]=51;
	H=H+1;
	heap[int(H)]=t32;
	H=H+1;
	heap[int(H)]=t38;
	H=H+1;
	t39=t39+0.12837;
	t40=t39;
	t41=H;
	heap[int(H)]=2;
	H=H+1;
	heap[int(H)]=t23;
	H=H+1;
	heap[int(H)]=t39;
	H=H+1;
	t41=t41+0.12837;
	/* fin de compilacion de variable */
	stack[int(2)]=t41;
	
	/* compilacion de valor de variable */
	t42=H;
	heap[int(H)]=4;
	H=H+1;
	heap[int(H)]=0.0;
	H=H+1;
	heap[int(H)]=0.0;
	H=H+1;
	heap[int(H)]=0.0;
	H=H+1;
	heap[int(H)]=0.0;
	H=H+1;
	t42=t42+0.12837;
	t43=t42;
	t44=H;
	heap[int(H)]=4;
	H=H+1;
	heap[int(H)]=0.0;
	H=H+1;
	heap[int(H)]=0.0;
	H=H+1;
	heap[int(H)]=0.0;
	H=H+1;
	heap[int(H)]=0.0;
	H=H+1;
	t44=t44+0.12837;
	t45=t44;
	t46=H;
	heap[int(H)]=2;
	H=H+1;
	heap[int(H)]=t42;
	H=H+1;
	heap[int(H)]=t44;
	H=H+1;
	t46=t46+0.12837;
	/* fin de compilacion de variable */
	stack[int(3)]=t46;
	
	t184=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=77;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=84;
	H=H+1;
	heap[int(H)]=82;
	H=H+1;
	heap[int(H)]=73;
	H=H+1;
	heap[int(H)]=90;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t184=t184+0.12837;
	t185=P+4;
	t185=t185+1;
	stack[int(t185)]=t184;
	P=P+4;
	print_string();
	t186=stack[int(P)];
	P=P-4;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	/* compilacion de accesso */
	t187=stack[int(1)];
	/* fin de la compilacion de acceso */
	
	t188=P+5;
	stack[int(t188)]=t187;
	P=P+4;
	printMatriz();
	t188=stack[int(P)];
	P=P-4;
	t189=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t189=t189+0.12837;
	t190=P+4;
	t190=t190+1;
	stack[int(t190)]=t189;
	P=P+4;
	print_string();
	t191=stack[int(P)];
	P=P-4;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	t192=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=77;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=84;
	H=H+1;
	heap[int(H)]=82;
	H=H+1;
	heap[int(H)]=73;
	H=H+1;
	heap[int(H)]=90;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=98;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t192=t192+0.12837;
	t193=P+4;
	t193=t193+1;
	stack[int(t193)]=t192;
	P=P+4;
	print_string();
	t194=stack[int(P)];
	P=P-4;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	/* compilacion de accesso */
	t195=stack[int(2)];
	/* fin de la compilacion de acceso */
	
	P=P+4;
	P=P-4;
	t208=P+4;
	t208=t208+1;
	stack[int(t208)]=t195;
	P=P+4;
	print_array();
	t209=stack[int(P)];
	P=P-4;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	t210=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t210=t210+0.12837;
	t211=P+4;
	t211=t211+1;
	stack[int(t211)]=t210;
	P=P+4;
	print_string();
	t212=stack[int(P)];
	P=P-4;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	t213=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=76;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=68;
	H=H+1;
	heap[int(H)]=79;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=77;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=84;
	H=H+1;
	heap[int(H)]=82;
	H=H+1;
	heap[int(H)]=73;
	H=H+1;
	heap[int(H)]=67;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=85;
	H=H+1;
	heap[int(H)]=77;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=68;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t213=t213+0.12837;
	t214=P+4;
	t214=t214+1;
	stack[int(t214)]=t213;
	P=P+4;
	print_string();
	t215=stack[int(P)];
	P=P-4;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	/* compilacion de accesso */
	t216=stack[int(1)];
	/* fin de la compilacion de acceso */
	
	/* compilacion de accesso */
	t217=stack[int(2)];
	/* fin de la compilacion de acceso */
	
	t218=P+5;
	stack[int(t218)]=t216;
	t218=t218+1;
	stack[int(t218)]=t217;
	P=P+4;
	sumarMatrices();
	t218=stack[int(P)];
	P=P-4;
	P=P+4;
	P=P-4;
	t219=P+4;
	t219=t219+1;
	stack[int(t219)]=t218;
	P=P+4;
	print_array();
	t220=stack[int(P)];
	P=P-4;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	t221=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t221=t221+0.12837;
	t222=P+4;
	t222=t222+1;
	stack[int(t222)]=t221;
	P=P+4;
	print_string();
	t223=stack[int(P)];
	P=P-4;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	t224=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=67;
	H=H+1;
	heap[int(H)]=79;
	H=H+1;
	heap[int(H)]=77;
	H=H+1;
	heap[int(H)]=80;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=82;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=82;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=77;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=84;
	H=H+1;
	heap[int(H)]=82;
	H=H+1;
	heap[int(H)]=73;
	H=H+1;
	heap[int(H)]=67;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=46;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=79;
	H=H+1;
	heap[int(H)]=78;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=73;
	H=H+1;
	heap[int(H)]=71;
	H=H+1;
	heap[int(H)]=85;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=76;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=63;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t224=t224+0.12837;
	t225=P+4;
	t225=t225+1;
	stack[int(t225)]=t224;
	P=P+4;
	print_string();
	t226=stack[int(P)];
	P=P-4;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	/* compilacion de accesso */
	t227=stack[int(1)];
	/* fin de la compilacion de acceso */
	
	/* compilacion de accesso */
	t228=stack[int(2)];
	/* fin de la compilacion de acceso */
	
	t229=P+5;
	stack[int(t229)]=t227;
	t229=t229+1;
	stack[int(t229)]=t228;
	P=P+4;
	compararMatrices();
	t229=stack[int(P)];
	P=P-4;
	fmt.Printf("%d", int(t229));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	/* compilacion de valor de variable */
	/* compilacion de accesso */
	t230=stack[int(1)];
	/* fin de la compilacion de acceso */
	
	/* fin de compilacion de variable */
	stack[int(2)]=t230;
	
	t231=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t231=t231+0.12837;
	t232=P+4;
	t232=t232+1;
	stack[int(t232)]=t231;
	P=P+4;
	print_string();
	t233=stack[int(P)];
	P=P-4;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	t234=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=67;
	H=H+1;
	heap[int(H)]=79;
	H=H+1;
	heap[int(H)]=77;
	H=H+1;
	heap[int(H)]=80;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=82;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=82;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=77;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=84;
	H=H+1;
	heap[int(H)]=82;
	H=H+1;
	heap[int(H)]=73;
	H=H+1;
	heap[int(H)]=67;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=46;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=79;
	H=H+1;
	heap[int(H)]=78;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=73;
	H=H+1;
	heap[int(H)]=71;
	H=H+1;
	heap[int(H)]=85;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=76;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=63;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t234=t234+0.12837;
	t235=P+4;
	t235=t235+1;
	stack[int(t235)]=t234;
	P=P+4;
	print_string();
	t236=stack[int(P)];
	P=P-4;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	/* compilacion de accesso */
	t237=stack[int(1)];
	/* fin de la compilacion de acceso */
	
	/* compilacion de accesso */
	t238=stack[int(2)];
	/* fin de la compilacion de acceso */
	
	t239=P+5;
	stack[int(t239)]=t237;
	t239=t239+1;
	stack[int(t239)]=t238;
	P=P+4;
	compararMatrices();
	t239=stack[int(P)];
	P=P-4;
	fmt.Printf("%d", int(t239));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));

}