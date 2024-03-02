def main_f():    
    import matplotlib
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Button
    from matplotlib.widgets import Slider
    # initial values
    Lion_num = 0
    Humans_num = 100
    infant_mortality = 10
    Lioninf_mortality = 20
    youth_mortality = 5
    agriculture = 5
    disas_chance = 10
    min_age_fert = 18
    max_age_fert = 60
    food = 1000
    mutation = 1  # Initial value for mutation
    rain = 1  # Initial value for rain factor

    fig, ax = plt.subplots()
    # for rain 
    def update_rain(val):
        global rain
        rain = val

    ax_rain = plt.axes([0.25, 0.8, 0.15, 0.03])
    rain_slider = Slider(ax_rain, 'Rain', valmin=0, valmax=2.5, valinit=rain)
    rain_slider.on_changed(update_rain)

    def update_Lion_num(val):
        global Lion_num
        Lion_num = val

    ax_Lion_num = plt.axes([0.50, 0.8, 0.15, 0.03])
    Lion_num_slider = Slider(ax_Lion_num, 'Lion_num', valmin=0, valmax=100, valinit=Lion_num,valstep=1)
    Lion_num_slider.on_changed(update_Lion_num)
    
    def update_Humans_num(val):
        global Humans_num
        Humans_num = val

    ax_Humans_num = plt.axes([0.25, 0.7, 0.15, 0.03])
    Humans_num_slider = Slider(ax_Humans_num, 'Humans_num', valmin=0, valmax=200, valinit=Humans_num,valstep=1)
    Humans_num_slider.on_changed(update_Humans_num)
    
    def update_infant_mortality(val):
        global infant_mortality
        infant_mortality = val

    ax_infant_mortality = plt.axes([0.50, 0.7, 0.15, 0.03])
    infant_mortality_slider = Slider(ax_infant_mortality, 'infant_mortality', valmin=0, valmax=100, valinit=infant_mortality)
    infant_mortality_slider.on_changed(update_infant_mortality)
    
    def update_Lioninf_mortality(val):
        global Lioninf_mortality
        Lioninf_mortality = val

    ax_Lioninf_mortality = plt.axes([0.25, 0.6, 0.15, 0.03])
    Lioninf_mortality_slider = Slider(ax_Lioninf_mortality, 'Lioninf_mortality', valmin=0, valmax=100, valinit=Lioninf_mortality)
    Lioninf_mortality_slider.on_changed(update_Lioninf_mortality)
    
    def update_youth_mortality(val):
        global youth_mortality
        youth_mortality = val

    ax_youth_mortality = plt.axes([0.50, 0.6, 0.15, 0.03])
    youth_mortality_slider = Slider(ax_youth_mortality, 'youth_mortality', valmin=0, valmax=100, valinit=youth_mortality)
    youth_mortality_slider.on_changed(update_youth_mortality)
    
    def update_disas_chance(val):
        global disas_chance
        disas_chance = val

    ax_disas_chance = plt.axes([0.25, 0.5, 0.15, 0.03])
    disas_chance_slider = Slider(ax_disas_chance, 'disas_chance', valmin=0, valmax=15, valinit=disas_chance)
    disas_chance_slider.on_changed(update_disas_chance)

    def update_food(val):
        global food
        food = val

    ax_food = plt.axes([0.50, 0.5, 0.15, 0.03])
    food_slider = Slider(ax_food, 'food', valmin=0, valmax=200, valinit=food)
    food_slider.on_changed(update_food)

    def update_mutation(val):
        global mutation
        mutation = val

    ax_mutation = plt.axes([0.25, 0.4, 0.15, 0.03])
    mutation_slider = Slider(ax_mutation, 'mutation', valmin=0, valmax=5, valinit=mutation)
    mutation_slider.on_changed(update_mutation)


    plt.show()
    print(Lion_num,Humans_num,infant_mortality,Lioninf_mortality,youth_mortality,agriculture,disas_chance,min_age_fert,max_age_fert,food,mutation,rain
)
    return Lion_num,Humans_num,infant_mortality,Lioninf_mortality,youth_mortality,agriculture,disas_chance,min_age_fert,max_age_fert,food,mutation,rain

