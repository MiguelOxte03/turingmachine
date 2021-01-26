from turingmachine import turing_M

print("Maquina de turing 1")
# Ejercicio Numero 3 del sigueinte enlace
# https://www.matesfacil.com/automatas-lenguajes/Maquina-Turing.html
# Entradas (No acepta 1 de entrada inicial)
# 0101
# 00110011
# 0
# 01010101
turing_M(state='q0',  # estado inicial
         blank='b',  # variable por defecto de la cinta
         tape=list("0101"),  # entradas del automata
         final='q4',  # estado de aceptacion
         # reglas de transicion
         rules=map(tuple,
                   [
                       "q0 Y Y right q0".split(),
                       "q0 b b right q4".split(),
                       "q0 0 X right q1".split(),
                       "q1 0 0 right q1".split(),
                       "q1 Y Y right q3".split(),
                       "q1 1 Y left q2".split(),
                       "q3 Y Y right q3".split(),
                       "q3 1 Y left q2".split(),
                       "q2 Y Y left q2".split(),
                       "q2 0 0 left q2".split(),
                       "q2 X X right q0".split(),
                   ]
                   )
         )
