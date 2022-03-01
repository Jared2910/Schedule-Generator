if __name__ == '__main__':
    from GeneadorDeHorario import GeneradorDeHorario
    from InventarioCursos import InventarioCursos

    inventario = InventarioCursos()
    
    inventario.agregarCurso("Programacion 4","41738","EIF209","Profesor 1","Lunes","13:00","14:40","Jueves","13:00","14:40")
    inventario.agregarCurso("Programacion 4","41739","EIF209","Profesor 2","Lunes","15:00","16:40","Jueves","15:00","16:40")
    inventario.agregarCurso("Programacion 4","41740","EIF209","Profesor 3","Lunes","18:00","19:40","Jueves","18:00","19:40")

    inventario.agregarCurso("Ingenieria en sistemas 1","41746","EIF210","Profesor 4","Miercoles","13:00","16:20")
    inventario.agregarCurso("Ingenieria en sistemas 1","41748","EIF210","Profesor 5","Viernes","13:00","16:40")

    inventario.agregarCurso("Bases de datos","41749","EIF211","Profesor 6","Lunes","10:00","11:40","Jueves","10:00","11:40")
    inventario.agregarCurso("Bases de datos","41750","EIF211","Profesor 7","Lunes","13:00","14:40","Jueves","13:00","14:40")
    inventario.agregarCurso("Bases de datos","41755","EIF211","Profesor 8","Martes","18:00","19:40","Viernes","18:00","19:40")

    inventario.agregarCurso("Metodos de investigacion","41784","EIF413","Profesor 9","Lunes","18:00","19:40","Jueves","18:00","19:40")
    inventario.agregarCurso("Metodos de investigacion","41786","EIF413","Profesor 10","Martes","15:00","16:40","Viernes","15:00","16:40")
    inventario.agregarCurso("Metodos de investigacion","41787","EIF413","Profesor 11","Martes","18:00","19:40","Viernes","18:00","19:40")
    inventario.agregarCurso("Metodos de investigacion","41789","EIF413","Profesor 12","Martes","13:00","14:40","Viernes","13:00","14:40")



    generador = GeneradorDeHorario(inventario)

    result = generador.BuscarCombinaciones()

    simplificada = generador.simplificar(result)

    final = generador.filtrarHorario(simplificada)

    generador.exportar_txt(final)

    #generador.imprimirHorarios(final)