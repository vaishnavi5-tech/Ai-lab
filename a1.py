def reflix_vaccum_agent(location,status):
    if status=="Dirty":
        return "suck"
    elif location =="A":
        return "Rigth"
    elif location=="B":
        return "Left"
location="A"
status="Dirty"
action=reflix_vaccum_agent(location,status)
print(f"Location:{location},status:{status},Action:{action}")