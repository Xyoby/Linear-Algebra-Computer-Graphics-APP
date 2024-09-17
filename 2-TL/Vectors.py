from manim import *

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        self.add(numberplane, dot, arrow, origin_text, tip_text)


from manim import *

class VectorArrowRotate(Scene):
    def construct(self):
        # Crear el plano de números
        numberplane = NumberPlane()
        self.add(numberplane)

        # Esperar un poco antes de aplicar la rotación
        self.wait(1)

        # Crear un vector
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0, color=BLUE)



        # Crear una matriz de transformación (rotación de 30 grados)
        rotation_matrix = np.array([[np.cos(np.pi / 6), -np.sin(np.pi / 6), 0],
                                    [np.sin(np.pi / 6), np.cos(np.pi / 6), 0],
                                    [0, 0, 1]])

        # Aplicar la transformación al vector
        transformed_arrow = arrow.copy().apply_matrix(rotation_matrix)

        # Crear el plano de números
        numberplane = NumberPlane()

        # Animación: Mostrar el vector original y su transformación
        self.play(Create(arrow))
        self.wait(1)
        self.play(Transform(arrow, transformed_arrow))
        self.wait(1)

        # Animación: Girar todo el plano de números
        self.play(Rotate(numberplane, angle=np.pi / 6, about_point=ORIGIN))
        self.wait(1)

        # Mostrar texto
        origin_text = Text('(0, 0)').next_to(arrow.get_start(), DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        self.add(numberplane, arrow, origin_text, tip_text)

        self.wait(2)  # Esperar un poco antes de finalizar

