class Texto():
    def _init_(self, texto):
        self.__texto = texto
        self._textito = self._texto.lower()

    def get_textito(self):
        return self.__textito

    def separador(self, c):
        self.separada = self.get_textito().split(c)
        

    def quit_rep(self):
        self.quit = []
        contador = 0
        for i in range(0, len(self.separada)):
            for j in range(i+1, len(self.separada)-1) :
                if self.separada[i] == self.separada[j]:
                    self.quit.append(j)

        for i in self.quit :
            self.separada.remove(self.separada[i - contador])
            contador += 1

        return self.separada


    def ordenar_eleccion(self):
        for i in range(0, len(self.separada)):
            mini = i
            for j in range(i+1 , len(self.separada)):
                if self.separada[j] < self.separada[mini]:
                    mini = j

            ayuda = self.separada[i]
            self.separada[i] = self.separada[mini]
            self.separada[mini] = ayuda


        return self.separada
            





a = Texto('Adventures in Disneyland Two blondes were going to Disneyland when they came to a fork in the road. The sign read: "Disneyland LEFT." So they went home.')

a.separador(' ')

print(a.quit_rep())

print(a.ordenar_eleccion())
#replace all
