conf_leds = {1:2,
             2:5,
             3:5,
             4:4,
             5:5,
             6:6,
             7:3,
             8:7,
             9:6,
             0:6
}


#iter_confs_keys = list(conf_leds.keys())
#iter_confs_values = list(conf_leds.values())

#print(conf_leds.get(1))




q1 = int(input("Ingrese el numero: "))


if q1 >= 0:
    q1_list = []
    q1_list.append(q1)
    q1_map = list(map(int, str(q1_list[0])))
    
    list_values = []

    for i in q1_map:
        values_conf = conf_leds.get(i)

        if len(list_values) < len(q1_map):
            list_values.append(values_conf)
    
            sum_values = sum(list_values)
else:
    print("El numero ingresado no es correcto")            

print(f"{sum_values} LEDs")

             


                

    

        
        
        





