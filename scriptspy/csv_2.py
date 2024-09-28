import csv
import os
import tkinter as tk
from tkinter import filedialog


header = ["LEVEL", "BOOST_VALUE", "BOOST_TYPE"]
item_name = ['standard_cannon','blast_cannon','sniper_cannon','explosive_cannon','galting_gun','carronade','grenade_launcher',
             'standard_mortar','long_range_mortar','ballpark_mortar','big_berta','standard_torpedo','big_torpedo','swift_torpedo',
             'triple_torpedo','railgun','missile_launcher','multi_missile','mine','flare_gun','napalm_launcher','fire_bomb',
             'standard_shield','big_shield','turbo','bandage','big_bandage','overboost','nitro','tesla_bolt','tesla_shield',
             'frost_blaster','frost_launcher','repair_box_launcher','repair_pulse','duct_tape','repair_bolt',
             'repair_plasma','defence_wall','defence_aura','bloster_armor','cleanse_pulse']
number_of_boosts = [
    32,#standard_cannon
    31,#blast_cannon
    30,#sniper_cannon
    30,#explosive_canon
    22,#galting_gun
    33,#carronade
    30,#grenade_launcher
    27,#standard_mortar
    28,#long_range_mortar
    27,#ballpark_mortar
    32,#big_berta
    31,#standard_torpedo
    27,#big_torpedo
    31,#swift_torpedo
    30,#triple_torpedo
    20,#railgun
    26,#missile_launcher
    26,#multi_missile
    28,#mine
    33,#flare_gun
    29,#napalm_launcher
    24,#fire_bomb
    27,#standard_shield
    30,#big_shield
    4,#turbo
    13,#bandage
    13,#big_bandage
    8,#overboost
    25,#nitro
    18,#tesla_bolt
    23,#tesla_shield
    13,#frost_blaster
    16,#frost_launcher
    29,#repair_box_launcher
    19,#repair_pulse
    15,#duct_tape
    17,#repair_bolt
    29,#repair_plasma
    27,#defence_wall
    13,#defence_aura
    13,#bloster_armor
    4#cleanse_pulse
]
boost_value = [
    [5,1,0.05,0.10,10,0.10,0.20,0.05,0.05,2,0.05,0.05,0.05,0.10,0.10,0.05,0.03,0.03,0.10,0.15,0.05,0.02,0.05,0.10,0.03,0.10,0.02,0.02,0.05,0.02,0.02,0.05],#standard_cannon
    [5,3,10,0.10,0.05,0.05,0.02,0.05,0.05,0.05,0.05,0.10,0.10,0.05,0.05,0.02,0.05,0.05,0.02,0.10,0.02,0.10,0.02,0.10,0.02,10,0.02,0.10,0.05,0.10,0.10],#blast_cannon
    [5,0.05,3,10,0.10,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.03,0.25,0.10,0.25,0.05,0.03,0.02,0.05,0.02,0.10,0.10,0.05,0.10,0.05,0.05,0.05,0.10,0.05],#sniper_cannon
    [5,0.05,3,0.10,0.05,0.05,10,0.05,0.05,0.05,0.05,0.05,0.05,0.10,0.10,0.05,0.05,0.05,0.05,0.10,0.10,0.05,0.05,0.05,0.05,0.05,0.05,0.10,0.05,0.05],#explosive_canon
    [2,1,4,0.05,1,0.05,0.05,0.05,0.05,1,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05],#galting_gun
    [0.05,1,0.05,0.02,0.05,1,0.05,0.02,0.05,0.30,0.02,1,0.05,0.30,0.02,0.05,0.20,1,0.05,0.05,0.02,0.02,0.05,0.05,0.20,1,0.05,0.05,0.05,1,1,0.02,0.10],#carronade
    [5,1,5,0.20,0.05,0.05,0.05,1,0.05,0.05,0.02,0.10,0.05,0.02,0.20,2,0.05,0.10,0.05,0.05,0.05,0.20,0.02,2,0.02,0.20,0.02,0.10,0.10,0.20],#grenade_launcher
    [0.05,5,0.05,5,0.05,0.05,1,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.30,0.05,0.05,0.05,0.05,0.05,0.05,2,0.05,0.05,0.05,0.05],#standard_mortar
    [5,2,0.05,5,0.05,0.05,0.05,0.02,0.05,0.10,0.05,0.05,0.02,0.05,0.05,0.05,0.030,0.02,0.05,0.02,0.05,0.02,1,0.05,0.05,0.05,0.05,0.05],#long_range_mortar
    [5,0.05,5,0.05,0.05,0.10,0.2,0.30,0.10,0.05,0.05,0.02,0.05,0.05,0.05,1,0.10,0.02,0.05,0.05,0.05,2,0.05,0.02,0.05,0.05,0.05],#ballpark_mortar
    [5,2,5,0.10,0.05,0.05,0.05,0.05,0.05,0.02,0.05,0.02,0.05,0.05,0.05,0.02,0.05,0.02,0.05,0.02,0.30,0.10,0.02,0.02,0.05,0.10,1,0.05,0.02,0.10,0.05,0.10],#big_berta
    [0.05,0.05,0.05,0.20,0.10,25,0.05,25,0.20,25,25,0.05,0.10,0.02,0.10,0.05,0.02,0.05,0.05,0.10,0.02,0.10,0.02,0.05,0.05,0.10,0.10,0.10,0.02,0.20,0.02],#standard_torpedo
    [25,0.05,25,0.10,0.10,0.05,25,0.05,0.10,0.10,0.10,0.05,0.02,0.10,0.05,0.10,0.02,0.10,0.02,0.05,0.10,0.05,0.10,0.05,0.02,0.10,0.02],#big_torpedo
    [0.05,0.05,0.05,0.20,0.10,25,0.05,25,0.20,25,25,0.05,0.10,0.02,0.10,0.05,0.02,0.05,0.05,0.10,0.02,0.10,0.02,0.05,0.05,0.10,0.10,0.10,0.02,0.20,0.02],#swift_torpedo
    [0.05,0.05,0.05,0.10,25,0.05,25,0.10,25,25,0.05,0.10,0.02,0.05,0.05,0.02,0.05,0.05,0.10,0.02,0.10,0.05,0.02,0.10,0.05,0.10,0.02,0.05,0.10,0.02],#triple_torpedo
    [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05],#railgun
    [0.05,1,0.05,0.05,0.02,0.05,0.02,0.05,0.05,0.02,0.02,0.05,0.05,0.05,0.02,0.02,2,0.05,0.02,0.05,0.05,0.05,0.02,0.05,0.05,0.05],#missile_launcher
    [0.05,1,0.05,0.05,0.02,0.05,0.02,0.05,0.05,0.02,0.02,0.05,0.05,0.05,0.02,0.02,2,0.05,0.02,0.05,0.05,0.05,0.02,0.05,0.05,0.05],#multi_missile
    [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,1,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.02,0.05,0.05,2,0.05,0.05,0.05],#mine
    [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,1,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,2,0.05,0.05,0.05,0.05,0.02,0.05,0.05],#flare_gun
    [0.05,0.05,0.05,0.10,0.05,0.10,0.05,0.10,0.05,0.10,1,0.10,0.05,0.05,0.05,0.05,0.05,0.05,0.05,2,0.05,0.05,0.05,0.05,0.05,0.010,0.05,0.05,0.05],#napalm_launcher
    [1,0.05,0.05,1,0.02,0.02,0.05,1,0.05,1,0.05,2,0.05,0.05,1,0.05,0.02,0.05,0.02,1,0.05,0.02,0.05,0.05],#fire_bomb
    [10,10,0.05,10,0.05,10,10,0.05,10,0.05,10,10,10,0.05,10,10,10,0.05,10,10,10,10,10,10,10,0.05,10],#standard_shield
    [5,5,0.05,5,0.05,5,5,0.05,5,0.05,5,5,5,0.05,5,5,5,0.05,5,5,5,5,5,5,5,0.05,5,0.05,0.05,0.05],#big_shield
    [0.05,0.05,0.05,0.05],#turbo
    [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05],#bandage
    [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05],#big_bandage
    [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05],#overboost
    [0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02],#nitro
    [0.02,0.05,0.02,0.05,0.02,0.05,0.02,0.05,0.02,1.0,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05],#tesla_bolt
    [25,0.03,0.05,25,0.03,25,0.05,25,0.03,0.05,0.03,0.05,0.03,0.05,0.03,0.05,0.03,0.05,0.03,0.05,0.03,0.03,0.05],#tesla_shield
    [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.50,0.05,0.05,0.05,0.05,0.05],#frost_blaster
    [0.05,0.02,0.05,0.02,0.05,0.02,0.05,0.02,0.05,0.02,0.05,0.02,0.05,0.02,0.05,0.02],#frsot_launcher
    [0.10,0.05,0.05,1,0.05,0.10,1,0.05,0.010,0.05,0.05,1,0.05,0.10,0.05,0.05,0.10,0.10,1,0.05,0.05,0.10,0.05,0.10,0.05,0.05,1,0.10,0.10],#repair_box_launcher
    [0.05,0.05,0.03,0.05,0.05,0.03,0.05,0.05,0.03,0.05,0.05,0.03,0.05,0.05,0.05,0.05,0.03,0.05,0.05],#repair_pulse
    [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05],#duct_tape
    [0.05,0.05,0.05,0.05,1.00,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,1.00,0.05,0.05,0.05],#repair_bolt
    [0.05,0.05,0.05,0.10,0.05,0.10,0.05,0.10,0.05,0.10,1,0.10,0.05,0.05,0.05,0.05,0.05,0.05,0.05,2,0.05,0.05,0.05,0.05,0.05,0.10,0.05,0.05,0.05],#repair_plasma
    [10,10,0.05,0.05,0.05,0.05,10,0.05,10,0.05,10,10,10,0.05,10,10,10,0.05,10,10,0.05,10,10,10,10,0.05,10],#defence_wall
    [0.05,0.01,0.01,0.05,0.01,0.05,0.01,0.05,0.01,0.01,0.05,0.01,0.05],#defence_aura
    [0.05,0.01,0.05,0.01,0.05,0.01,0.05,0.01,0.05,0.01,0.01,0.05,0.01],#bloster_armor
    [0.05,0.05,0.05,0.05]#cleanse_pulse
]

boost_type = [
    ['BASE_STAT','RANGE','FIRE_DAMAGE','COOL_DOWN','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','RANGE','BASE_STAT','RANGE','BASE_STAT','FIRE_DAMAGE','BASE_STAT','COOL_DOWN','PROJECTILE_SPEED','FIRE_DAMAGE','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','FIRE_DAMAGE','BASE_STAT','RANGE','COOL_DOWN','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','FIRE_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT'],#standard_cannon
    ['BASE_STAT','RANGE','BASE_STAT','PROJECTILE_SPEED','FIRE_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','RANGE','FIRE_DAMAGE','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','FIRE_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','RANGE','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','BASE_STAT','FIRE_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','BASE_STAT'],#blast_cannon
    ['BASE_STAT','FIRE_DAMAGE','RANGE','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','CRITICAL_HIT_CHANCE','BASE_STAT','BASE_STAT','FIRE_DAMAGE','CRITICAL_HIT_CHANCE','RANGE','CRITICAL_HIT_DAMAGE','PROJECTILE_SPEED','CRITICAL_HIT_DAMAGE','FIRE_DAMAGE','RANGE','BASE_STAT','FIRE_DAMAGE','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','FIRE_DAMAGE','BASE_STAT','PROJECTILE_SPEED','BASE_STAT'],#sniper_cannon
    ['BASE_STAT','FIRE_DAMAGE','RANGE','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','FIRE_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','FIRE_DAMAGE','RANGE','BASE_STAT','FIRE_DAMAGE','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','FIRE_DAMAGE','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT'],#explosive_canon
    ['BASE_STAT','RANGE','BASE_STAT','COOL_DOWN','RANGE','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','RANGE','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','COOL_DOWN','RANGE','BASE_STAT','COOL_DOWN','RANGE','BASE_STAT','COOL_DOWN','BASE_STAT'],#galting_gun
    ['BASE_STAT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT','FROST_EFFECT','BASE_STAT','RANGE','BASE_STAT','TURET_ROTATION','BASE_STAT','BASE_STAT','FROST_EFFECT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','TURET_ROTATION','BASE_STAT','FROST_EFFECT','RANGE','BASE_STAT','TURET_ROTATION','BASE_STAT','RANGE','RANGE','BASE_STAT','TURET_ROTATION'],#carronade
    ['BASE_STAT','RANGE','BASE_STAT','CRITICAL_HIT_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT','CRITICAL_HIT_CHANCE','BASE_STAT','BASE_STAT','CRITICAL_HIT_DAMAGE','RANGE','BASE_STAT','CRITICAL_HIT_CHANCE','BASE_STAT','BASE_STAT','BASE_STAT','CRITICAL_HIT_DAMAGE','BASE_STAT','RANGE','BASE_STAT','CRITICAL_HIT_DAMAGE','BASE_STAT','CRITICAL_HIT_CHANCE','BASE_STAT','CRITICAL_HIT_DAMAGE'],#grenade_launcher
    ['COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','RANGE','BASE_STAT','FROST_DAMAGE','COOL_DOWN','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','CRITICAL_HIT_DAMAGE','COOL_DOWN','BASE_STAT','FROST_DAMAGE','BASE_STAT','RANGE','BASE_STAT','FROST_DAMAGE','COOL_DOWN','BASE_STAT'],#standard_mortar
    ['BASE_STAT','RANGE','FROST_DAMAGE','BASE_STAT','FROST_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','FROST_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','CRITICAL_HIT_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','RANGE','BASE_STAT','PROJECILE_SPEED','PROJECTILE_SPEED','FROST_DAMAGE','BASE_STAT'],#long_range_mortar
    ['BASE_STAT','FROST_DAMAGE','BASE_STAT','FROST_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','CRITICAL_HIT_DAMAGE','BASE_STAT','FROST_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT'],#ballpark_mortar
    ['BASE_STAT','RANGE','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','CRITICAL_HIT_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT'],#big_berta
    ['COOL_DOWN','BASE_STAT','COOL_DOWN','PROJECTILE_SPEED','FROST_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','FROST_DAMAGE','PROJECTILE_SPEED','BASE_STAT','PROJECTILE_SPEED','BASE_STAT'],#standard_torpedo
    ['BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','BASE_STAT'],#big_torpedo
    ['COOL_DOWN','BASE_STAT','COOL_DOWN','PROJECTILE_SPEED','FROST_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','FROST_DAMAGE','PROJECTILE_SPEED','BASE_STAT','PROJECTILE_SPEED','BASE_STAT'],#swift_torpedo
    ['COOL_DOWN','BASE_STAT','COOL_DOWN','FROST_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','FROST_DAMAGE','BASE_STAT','BASE_STAT','PROJECTILE_SPEED','BASE_STAT'],#triple_torpedo
    ['BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT'],#railgun
    ['BASE_STAT','RANGE','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT'],#missile_launcher
    ['BASE_STAT','RANGE','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT'],#multi_missile
    ['BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','RANGE','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT'],#mine
    ['PROJECTILE_SPEED','BASE_STAT','DURATION','BASE_STAT','PROJECTILE_SPEED','DURATION','BASE_STAT','DURATION','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','HEALING_REDUCTION','DURATION','BASE_STAT','PROJECTILE_SPEED','RANGE','HEALING_REDUCTION','DURATION','BASE_STAT','BASE_STAT','HEALING_REDUCTION','BASE_STAT','DURATION','PROJECTILE_SPEED','HEALING_REDUCTION','RANGE','BASE_STAT','HEALING_REDUCTION','DURATION','PROJECTILE_SPEED','BASE_STAT','HEALING_REDUCTION','BASE_STAT'],#flare_gun
    ['BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT'],#napalm_launcher
    ['DURATION','BASE_STAT','COOL_DOWN','RANGE','BASE_STAT',  'BASE_STAT','BASE_STAT','DURATION','BASE_STAT','DURATION','BASE_STAT','RANGE','COOL_DOWN','BASE_STAT','DURATION','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','DURATION','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT'],#fire_bomb
    ['BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT'],#standard_shield
    ['BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT'],#big_shield
    ['BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT'],#turbo
    ['BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT'],#bandage
    ['BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT'],#big_bandage
    ['BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT'],#overboost
    ['BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','COOL_DOWN','COOL_DOWN','COOL_DOWN'],#nitro
    ['BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','HEALING_BLOCK','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT'],#tesla_bolt
    ['BASE_STAT','DURATION','BASE_STAT','BASE_STAT','DURATION','BASE_STAT','BASE_STAT','BASE_STAT','DURATION','BASE_STAT','DURATION','BASE_STAT','DURATION','BASE_STAT','DURATION','BASE_STAT','DURATION','BASE_STAT','DURATION','BASE_STAT','DURATION','DURATION','BASE_STAT'],#tesla_shield
    ['BASE_STAT','DURATION','COOL_DOWN','BASE_STAT','DURATION','BASE_STAT','COOL_DOWN','HEALING_REDUCTION','DURATION','BASE_STAT','COOL_DOWN','BASE_STAT','DURATION'],#frost_blaster
    ['DURATION','PROJECTILE_SPEED','DURATION','PROJECTILE_SPEED','BASE_STAT','PROJECTILE_SPEED','BASE_STAT','PROJECTILE_SPEED','DURATION','PROJECTILE_SPEED','BASE_STAT','PROJECTILE_SPEED','DURATION','PROJECTILE_SPEED','BASE_STAT','PROJECTILE_SPEED'],#frsot_launcher
    ['CRITICAL_HIT_CHANCE','BASE_STAT','COOL_DOWN','RANGE','BASE_STAT','CRITICAL_HIT_CHANCE','RANGE','BASE_STAT','CRITICAL_HIT_CHANCE','CRITICAL_HIT_CHANCE','BASE_STAT','RANGE','COOL_DOWN','CRITICAL_HIT_CHANCE','CRITICAL_HIT_CHANCE','BASE_STAT','CRITICAL_HIT_CHANCE','CRITICAL_HIT_CHANCE','RANGE','BASE_STAT','BASE_STAT','CRITICAL_HIT_CHANCE','COOL_DOWN','CRITICAL_HIT_CHANCE','CRITICAL_HIT_CHANCE','BASE_STAT','RANGE','CRITICAL_HIT_CHANCE','CRITICAL_HIT_CHANCE'],#repair_box_launcher
    ['BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT'],#repair_pulse
    ['BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT'],#duct_tape
    ['BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','REMOVE_STUN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','REMOVE_FROST','COOL_DOWN','COOL_DOWN','BASE_STAT'],#repair_bolt
    ['BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','RANGE','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','COOL_DOWN','COOL_DOWN','COOL_DOWN','COOL_DOWN'],#repair_plasma
    ['BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT','BASE_STAT'],#defence_wall
    ['COOL_DOWN','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN'],#defence_aura
    ['COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','COOL_DOWN','BASE_STAT','BASE_STAT','COOL_DOWN','BASE_STAT'],#bloster_armor
    ['COOL_DOWN','COOL_DOWN','COOL_DOWN','COOL_DOWN']#cleanse_pulse
]



# Function to prompt the user for the folder
def get_output_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder = filedialog.askdirectory(title="Select Folder to Save Files")
    return folder

# Get output folder from the user
output_folder = get_output_folder()

# Check if the folder was selected
if output_folder:
    for i in range(0, 42):
        file_name = item_name[i] + "_training.csv"
        full_path = os.path.join(output_folder, file_name)  # Create full file path
        print(f"Saving file to: {full_path}")
        with open(full_path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            num = number_of_boosts[i]
            writer.writerow([num])  # Convert num to a list
            writer.writerow(header)
            for j in range(num):
                writer.writerow([j+1, boost_value[i][j], boost_type[i][j]])
else:
    print("No folder selected. Exiting...")