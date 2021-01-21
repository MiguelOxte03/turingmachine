from turingmachine import turing_M

print("Maquina de turing 1")

turing_M (state = 'q0', #estado inicial de la maquina de turing
              blank = 'b', #simbolo blanco de el alfabeto dela cinta
              tape = list("1"),#inserta los elementos en la cinta
              final = 'q2',  #estado valido y/o final
              rules = map(tuple,#reglas de transicion
                          [
                          "q0 0 0 right q0".split(),
                          "q0 1 1 right q0".split(),
                          "q0 b b left q1".split(),
                          "q1 1 0 left q1".split(),
                          "q1 0 1 right q2".split(),
                          "q1 0 1 left q2".split(),
                          "q1 b 1 left q2".split(),
                          ]
                         )
             )

print("Maquina de turing 2")

turing_M (state = 'q0',
              blank = 'b',
              tape = list("111"),
              final = 'q2',
              rules = map(tuple,
                          [
                          "q0 0 0 right q0".split(),
                          "q0 1 1 right q0".split(),
                          "q0 b b left q1".split(),
                          "q1 1 0 left q1".split(),
                          "q1 0 1 right q2".split(),
                          "q1 0 1 left q2".split(),
                          "q1 b 1 left q2".split(),
                          ]
                         )
             )