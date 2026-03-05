sec= "AT  GC"

def contador_nucleotidos(sec):
    
    
    # Eliminar espacios en blanco y convertir a mayúsculas
    sec=sec.replace(" ", "")
    sec=sec.upper()
     
    
    
    longitud=len(sec)
    
    for char in sec:
        if char not in "ATCG":
            print(f"Caracter no valido: {char}")
            return
    
    if longitud>0:
        adenina=sec.count("A")
        timina=sec.count("T")
        citosina=sec.count("C")
        guanina=sec.count("G")

        
        print(f"A: {adenina}")
        print(f"T: {timina}")
        print(f"C: {citosina}")
        print(f"G: {guanina}")
    
    print(f"Longitud: {longitud}")
    
    
def porcentaje_cg(sec):
    sec=sec.replace(" ", "")
    sec=sec.upper()
    longitud=len(sec)
    
    if longitud == 0:
        print("Secuencia vacia")
        return
    
    pc_gc=(sec.count("C")+sec.count("G"))/longitud*100
    print(f"Porcentaje de C y G: {pc_gc:.2f}%")

contador_nucleotidos("AT   GC")
porcentaje_cg("AT   GCAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGATATCGATCGTCGTCGATCGATGCTAGCT")