temp=float(input("enter temperature in degrees celcius"))


if temp<15:
    advice="it's cold ___ wear a jacket"
elif 15 <= temp <=25:
    advice="The weather is pleasant __enjoy your day"
else:
    advice="It's hot__stay hydrated."

print(f"Advice:{advice}")       