import math

totalMinions = float(input())
rCockpit = float(input())
rBody, hBody = [float(i) for i in input().split(" ")]
podL, podW, podH = [float(i) for i in input().split(" ")]

#print('=============================')
#print('=============================')

vCockpit = (4/3) * math.pi * (math.pow(rCockpit, 3)) - 2.20 - 4.10
vBody = hBody * math.pi * (math.pow(rBody, 2)) - 12.10
vPods = 2 * ((1/3) * podL * podW * podH)
vMinions = totalMinions * 1.20

print("Cockpit {:.2f}".format(vCockpit))
print("Body {:.2f}".format(vBody))
print("Pods {:.2f}".format(vPods))
print("Minions Need {:.2f}".format(vMinions))

vForMinions = round((vCockpit + vBody + vPods), 2)

if (vForMinions >= vMinions):
    print("PLAN ACCEPTED")
else:
    print("PLAN REJECTED")