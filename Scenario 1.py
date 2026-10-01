#Name:Anthony Martinez
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

enemy1 = {
    'Tropinaux' : {
        'damage' : 40,
        'health' : 20000 ,
        'attackspd' : 3,
    },
    'ubmmew': {
        'damage' : 2500,
        'health' : 199191928239,
        'attackspd' : 4,
    },
    'flamefrags' : {
        'damage' : 450,
        'health' : 1,
        'attackspd' : 8, },
    'tonyman' : {
        'damage' : 2000000000000,
        'health' : 100000000,
        'attackspd' : 1234567, },
    'santiman' : {
        'damage' : 2,
        'Health' : 0.000001,
        'attackspd' : 1000000000000000000000000000000000,
    },
}



enemy1['santiman'].update({"damage" : int(input("Damagechanger3000::"))})
enemy1['tonyman'].update({"damage" : int(input("Damagechanger3000::"))})
enemy1['flamefrags'].update({"damage" : int(input("Damagechanger3000::"))})
enemy1['ubmmew'].update({"damage" : int(input("Damagechanger3000::"))})
enemy1['Tropinaux'].update({"damage" : int(input("Damagechanger3000::"))})
print (enemy1)