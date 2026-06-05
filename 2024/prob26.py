with open("input.txt", "r") as f:
    plan = f.readline().strip("\n").split(", ")

parsed_plan = {}
for stat in plan:
    name, i_stat = stat.split(":")
    parsed_plan[name] = float(i_stat.rstrip("m/s"))

# Preventing KeyErrors by assigning super high arbitary values
if "Door" not in parsed_plan:
    parsed_plan["Door"] = 100000000

if "Flashlight" not in parsed_plan:
    parsed_plan["Flashlight"] = 100000000

h_log, a_log = ["HERO:"], ["ANIMATRONIC:"]

def simulate():
    h_pos = 0.0
    a_pos = parsed_plan["Start"]
    time = 0

    blinded = False
    blind_count = 2

    blocked = False
    block_count = 3

    flashlight_used = False
    door_used = False

    while True:
        # Update Time
        t_str = "Time-"
        time += 1
        if time < 10:
            t_str += "0" + str(time)
        else:
            t_str += str(time)
        t_str += ": "

        # Update hero position
        h_str = str(h_pos)
        h_pos += parsed_plan["Run"]
        h_pos = round(h_pos, 1)
        h_str += ("->" + str(h_pos))


        # Update animatronic position
        a_str = ""
        if not blinded and not blocked:
            s = str(a_pos)
            a_pos += parsed_plan["Chase"]
            a_pos = round(a_pos, 1)
            s += ("->" + str(a_pos))

            a_str = s
        elif blinded:
            a_str = "blinded"
            blind_count -= 1
        else:
            a_str = "blocked"
            block_count -= 1
        
        # Check blind count
        if blind_count == 0:
            blinded = False

        # Check block count
        if block_count == 0:
            blocked = False
        
        # Now print updated positions
        h_log.append(t_str + h_str)
        a_log.append(t_str + a_str)
        
        # Player loss/win (tie goes to animatronic)
        if a_pos >= h_pos:
            h_log.append("OH NO!")
            a_log.append("CAUGHT!")
            return
        if h_pos >= parsed_plan["Length"]:
            h_log.append("MADE IT!")
            a_log.append("MISSED!")
            return
        
        # Hero interaction with door
        if h_pos >= parsed_plan["Door"] and not door_used:
            dist = parsed_plan["Door"]
            h_log.append(f"[door shut at {dist}]")
            door_used = True
        
        # Animatronic interaction with door
        if a_pos >= parsed_plan["Door"] and door_used and block_count == 3:
            a_pos = parsed_plan["Door"]
            a_log.append("[door, stopped]")
            blocked = True

        # Flashlight functionality
        if h_pos >= parsed_plan["Flashlight"]:
            if not flashlight_used and not h_pos > parsed_plan["Door"] >= a_pos:
                dist = parsed_plan["Flashlight"]
                blinded = True
                h_log.append(f"[flashlight used at {dist}]")
                a_log.append(f"[blinded, stopped]")

            flashlight_used = True



if __name__ == '__main__':
    simulate()
    [print(i) for i in h_log]
    print()
    [print(i) for i in a_log]