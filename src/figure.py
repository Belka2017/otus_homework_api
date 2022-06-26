class Figure:

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Переданная фигура не является геометрической или не была определена")
        if '_area' in figure.__dict__ and '_area' in self.__dict__:
            return self._area + figure._area
        else:
            raise ValueError("Фигура, которую вы передали, не является геометрической фигурой или не была определена")
