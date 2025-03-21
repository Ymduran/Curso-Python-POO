print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 20 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Encapsulamiento                                                  * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0):
        self.titular = titular
        self._saldo = saldo_inicial #proteger

    def depositar(self, cantidad: float) -> None:
        if cantidad > 0:
            self._saldo += cantidad
            print(f"El dinero fue agregado al saldo de {self.titular} con éxito.")

        else:
            print("Cantidad inválida.")

    def retirar(self,cantidad: float) -> None:
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"El dinero fue retirado del saldo de {self.titular} con éxito.")

    def __str__(self) -> str:
        return f"Titular: {self.titular} Saldo = {self._saldo}"

    # Para el mét0do get
    @property
    def saldo(self) -> float:
        return self._saldo

    # Para el mét0do set
    @saldo.setter
    def saldo(self, nuevo_saldo: float) -> None:
        self._saldo = nuevo_saldo


if __name__ == '__main__':
    cuenta_guadalupe = CuentaBancaria("Guadalupe",10)
    print(cuenta_guadalupe)
    cuenta_guadalupe.saldo = 5



