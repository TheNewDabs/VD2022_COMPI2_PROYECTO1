import ply.yacc as yacc
import ply.lex as lex



reservadas = {
    "println": "PRINTLN",
    "print": "PRINT",
    "while": "WHILE",
    "for": "FOR",
    "if": "IF",
    "in": "IN",
    "elseif": "ELSEIF",
    "else": "ELSE",
    "nothing": "NOTHING",
    "Int64": "INT",
    "Float64": "FLOAT",
    "Array": "ARRAY",
    "Bool": "BOOL",
    "Char": "CHAR",
    "String": "STRING",
    "struct": "STRUCT",
    "uppercase": "UPPERCASE",
    "lowercase": "LOWERCASE",
    "log10": "LOG10",
    "log": "LOG",
    "sin": "SIN",
    "cos": "COS",
    "tan": "TAN",
    "trunc": "TRUNC",
    "float": "TOFLOAT",
    "string": "TOSTRING",
    "parse": "PARSE",
    "typeof": "TYPEOF",
    "sqrt": "SQRT",
    "length": "LENGTH",
    "push": "PUSH",
    "pop": "POP",
    "function": "FUNCTION",
    "break": "BREAK",
    "continue": "CONTINUE",
    "return": "RETURN",
    "end": "END",
    "true": "TRUE",
    "false": "FALSE",
    "local": "LOCAL",
    "global": "GLOBAL"
}

tokens = [
    "PTCOMA",
    "DOSP",
    "PUNTO",
    "COMA",
    "CORCHETEIZQ",
    "CORCHETEDER",
    "PARIZQ",
    "PARDER",
    "IGUAL",
    "MAS",
    "MENOS",
    "POR",
    "DIVIDIDO",
    "POTENCIA",
    "MODULO",
    "MENQUE",
    "MENIGUALQUE",
    "MAYQUE",
    "MAYIGUALQUE",
    "OR",
    "AND",
    "NOT",
    "IGUALQUE",
    "NIGUALQUE",
    "DECIMAL",
    "ENTERO",
    "CADENA",
    "CARACTER",
    "ID"
] + list(reservadas.values())

# Tokens
t_PTCOMA = r';'
t_DOSP = r':'
t_PUNTO = r'\.'
t_COMA = r','
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r']'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_POTENCIA = r'\^'
t_MODULO = r'%'
t_MENQUE = r'<'
t_MENIGUALQUE = r'<='
t_MAYQUE = r'>'
t_MAYIGUALQUE = r'>='
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
t_IGUALQUE = r'=='
t_NIGUALQUE = r'!='
t_IGUAL = r'='


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reservadas.get(t.value, 'ID')
    return t


def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


def t_CARACTER(t):
    r'\'.\''
    t.value = t.value[1:-1]
    return t


# Comentario de múltiples líneas /* .. */


def t_COMENTARIO_MULTILINEA(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count('\n')


# Comentario simple // ...


def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    error_lexico = {}
    error_lexico["type"] = "lexico"
    error_lexico["value"] = "Caracter no reconocido " + t.value[0] + "\n"
    
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Construyendo el analizador léxico

lexer = lex.lex()

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IGUALQUE', 'NIGUALQUE'),
    ('left', 'MAYQUE', 'MENQUE', 'MAYIGUALQUE', 'MENIGUALQUE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO', 'MODULO'),
    ('left', 'POTENCIA'),
    ('right', 'UMENOS')
)


# Definición de la gramática


def p_init(t):
    '''init            : instrucciones'''
    t[0] = t[1]


def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion
                        | instruccion'''
    


def p_instruccion(t):
    '''instruccion      : print_instr PTCOMA
                        | println_instr PTCOMA
                        | definicion_instr PTCOMA
                        | asignacion_instr PTCOMA
                        | asignacion_arreglo_instr PTCOMA
                        | definicion_asignacion_instr PTCOMA
                        | call_function PTCOMA
                        | declare_function PTCOMA
                        | return_state PTCOMA
                        | break_state PTCOMA
                        | continue_state PTCOMA
                        | if_state PTCOMA
                        | while_state PTCOMA
                        | for_state PTCOMA
                        | nativas PTCOMA
                        | create_struct PTCOMA
                        | declare_struct PTCOMA
                        | assign_access PTCOMA'''
    


def p_expression(t):
    '''expression       : MENOS expression %prec UMENOS
                        | NOT expression %prec UMENOS
                        | expression MAS expression
                        | expression MENOS expression
                        | expression POR expression
                        | expression DIVIDIDO expression
                        | expression POTENCIA expression
                        | expression MODULO expression
                        | expression MAYQUE expression
                        | expression MENQUE expression
                        | expression MENIGUALQUE expression
                        | expression MAYIGUALQUE expression
                        | expression IGUALQUE expression
                        | expression NIGUALQUE expression
                        | expression OR expression
                        | expression AND expression
                        | final_expression'''
    

# todo falta potencia y modulo
def p_final_expression(t):
    '''final_expression     : PARIZQ expression PARDER
                            | CORCHETEIZQ exp_list CORCHETEDER
                            | DECIMAL
                            | ENTERO
                            | CADENA
                            | CARACTER
                            | ID
                            | ID index_list
                            | TRUE
                            | FALSE
                            | call_function
                            | access_struct
                            | nativas'''
    

def p_nativas(t):
    '''nativas          : LOG PARIZQ ENTERO COMA expression PARDER
                        | LOG10 PARIZQ expression PARDER
                        | COS PARIZQ expression PARDER
                        | SIN PARIZQ expression PARDER
                        | TAN PARIZQ expression PARDER
                        | SQRT PARIZQ expression PARDER
                        | UPPERCASE PARIZQ expression PARDER
                        | LOWERCASE PARIZQ expression PARDER
                        | TOSTRING PARIZQ expression PARDER
                        | TOFLOAT PARIZQ expression PARDER
                        | TRUNC PARIZQ INT COMA expression PARDER
                        | TRUNC PARIZQ expression PARDER
                        | TYPEOF PARIZQ expression PARDER
                        | PARSE PARIZQ tipo COMA expression PARDER
                        | LENGTH PARIZQ expression PARDER
                        | PUSH PARIZQ expression COMA expression PARDER
                        | POP PARIZQ expression PARDER
                        '''
    

def p_print_instr(t):
    'print_instr    : PRINT PARIZQ exp_list PARDER'
    


def p_println_instr(t):
    'println_instr  : PRINTLN PARIZQ exp_list PARDER'
   


def p_tipo(t):
    '''tipo     : INT
                | FLOAT
                | BOOL
                | CHAR
                | STRING
                | ARRAY
                | NOTHING
    '''
    


def p_definicion_instr(t):
    '''definicion_instr   :  LOCAL ID
                            | GLOBAL ID'''
    


def p_asignacion_instr(t):
    '''asignacion_instr     : ID IGUAL expression
                            | LOCAL ID IGUAL expression
                            | GLOBAL ID IGUAL expression'''
    


def p_definicion_asignacion_instr(t):
    '''definicion_asignacion_instr  : ID IGUAL expression DOSP DOSP tipo
                                    | LOCAL ID IGUAL expression DOSP DOSP tipo
                                    | GLOBAL ID IGUAL expression DOSP DOSP tipo'''
    

def p_asignacion_arreglo_instr(t):
    '''asignacion_arreglo_instr     : ID index_list IGUAL expression'''
    


# todo tengo que hacer que se asignar y declarar los arreglos con index

def p_call_function_instr(t):
    '''call_function    : ID PARIZQ PARDER
                        | ID PARIZQ exp_list PARDER'''
    


def p_exp_list_instr(t):
    '''exp_list         : exp_list COMA expression
                        | expression'''
    


def p_index_list_instr(t):
    '''index_list       : index_list CORCHETEIZQ expression CORCHETEDER
                        | CORCHETEIZQ expression CORCHETEDER'''
    


def p_statement(t):
    '''statement        : instrucciones'''
    


def p_declare_function(t):
    '''declare_function     : FUNCTION ID PARIZQ PARDER DOSP DOSP tipo statement END
                            | FUNCTION ID PARIZQ dec_params PARDER DOSP DOSP tipo statement END
                            | FUNCTION ID PARIZQ dec_params PARDER statement END
                            | FUNCTION ID PARIZQ PARDER statement END'''
    

def p_dec_params(t):
    '''dec_params :    dec_params COMA ID DOSP DOSP tipo
                    | dec_params COMA ID DOSP DOSP ID
                    | dec_params COMA ID
                    | ID DOSP DOSP tipo
                    | ID DOSP DOSP ID
                    | ID'''
    


def p_if_state(t):
    '''if_state     : IF expression statement END
                    | IF expression statement ELSE statement END
                    | IF expression statement else_if_list END'''
    

def p_else_if_list(t):
    '''else_if_list     : ELSEIF expression statement
                        | ELSEIF expression statement ELSE statement
                        | ELSEIF expression statement else_if_list'''
    

def p_while_state(t):
    '''while_state      : WHILE expression statement END'''
    

def p_for_state(t):
    '''for_state        : FOR ID IN expression DOSP expression statement END
                        | FOR ID IN expression statement END'''
    

def p_break(t):
    '''break_state      : BREAK'''
    

def p_continue(t):
    '''continue_state      : CONTINUE'''
    

def p_return(t):
    '''return_state     : RETURN
                        | RETURN expression'''
    

def p_createStruct(t):
    'create_struct : STRUCT ID attList END'
    

def p_attList(t):
    '''attList :  attList ID DOSP DOSP tipo PTCOMA
                | ID DOSP DOSP tipo PTCOMA'''
    

def p_declareStruct(t):
    'declare_struct : ID DOSP DOSP ID'
    

def p_assignAccess(t):
    'assign_access : ID PUNTO ID IGUAL expression'


def p_access_struct(t):
    '''access_struct : ID PUNTO ID'''


def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)


parser = yacc.yacc()


def parse(input):
    # f = open(
    #     "/home/juanpa/Documents/Compi/OLC2_Proyecto1/compiler/grammar/pruebas.jl", "r")
    # input = f.read()
    # todo esto lo tengo que cambiar para jalarlo en el endpoint
    return parser.parse(input, lexer=lexer)
