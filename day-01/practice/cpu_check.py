# apko kam krna hai ki user se threshold lena hai
# current cpu usage check krna hai
# agar cpu usage threshold se zyada hai to alert email send krna hai admin ko


import psutil

def get_cpu_usage():
    threshold = int(input("Enter CPU threshold percentage: "))
    
    current_cpu_usage = psutil.cpu_percent(interval=1)
    
    print("Current CPU Usage:", current_cpu_usage, "%")
    print("Threshold:", threshold, "%")

    if current_cpu_usage > threshold:
        print("⚠ CPU Alert! Email sent to admin...")
    else:
        print("✅ CPU in Safe state... No alert needed.")

get_cpu_usage()
    
 