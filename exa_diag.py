tot_v=0
mont_tot=0
s_n="si"
while s_n=="si":
        marca=input("Ingrese la marca")
        origen=input("Ingrese el origen").strip().lower()
        costo=float(input("Ingrese el costo"))
        if origen == "alemania":
            impuesto_porcentaje=0.20
        elif origen== "japon":
            impuesto_porcentaje+0.30
        elif origen== "italia":
            impuesto_porcentaje+0.15
        elif origen=="usa":
            impuesto_porcentaje==0.08
        else:
            impuesto_porcentaje=0
        impuesto=costo*impuesto_porcentaje
        p_venta=costo+impuesto
        tot_v+=1
        mont_tot+=p_venta
        print(f"Costo con impuesto{p_venta}\nimpuesto{impuesto}")
        s_n=input("otra captura").strip().lower()
print(f"total de vehiculos {tot_v}\n total de todos los vehiculos {mont_tot}")


   