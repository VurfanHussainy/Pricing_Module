from django.http import HttpResponse
from django.shortcuts import render
from urllib.parse import parse_qs


def get_distance_base_price(distance, day_of_week):
    if day_of_week in ['Tue', 'Wed', 'Thu','Fri']:
        return 80  # Rs 80 up to 3KMs
    elif day_of_week in ['Sat', 'Mon']:
        return 90  # Rs 90 up to 3.5KMs
    elif day_of_week == 'Sun':
        return 95  # Rs 95 up to 3.5KMs
    else:
        return 0  # Default or error case

def get_distance_additional_price(distance):
    if distance <= 3:
        return 0  # No additional price for the first 3 KMs
    else:
        return (distance - 3) * 30  # Rs 30 per additional KM

def get_time_multiplier_factor(total_time):
    if total_time <= 60:
        return 1.0  # 1x for the first hour
    elif total_time <= 120:
        return 1.25  # 1.25x for the second hour
    else:
        return 2.2  # 2.2x for subsequent hours

def get_waiting_charges(waiting_time):
    if waiting_time <= 180:
        return 0  # No waiting charges for the first 3 mins
    else:
        return ((waiting_time - 180) // 3) * 5  # Rs 5 for every 3 mins after the initial 3 mins

def calculate_price(distance, time, waiting_time, day_of_week):
    dbp = get_distance_base_price(distance, day_of_week)
    dap = get_distance_additional_price(distance)
    tmf = get_time_multiplier_factor(time)
    wc = get_waiting_charges(waiting_time)

    total_price = (dbp + dap) * tmf + wc
    return total_price


def calculate_price_view(request):
    # import pdb
    # pdb.set_trace()
    if request.method == 'POST':
        
        data = request.body.decode('utf-8')  
        print("data", data)
        parsed_data = parse_qs(data)

        # Convert the dictionary to a list of dictionaries
        data_list = [{key: value[0]} for key, value in parsed_data.items()]
        distance = None
        time = None
        days_of_week = None
        waiting_time = None
        for item in data_list:
            # Check if the key exists before assigning its value
            if 'distance' in item:
                distance = float(item['distance'])  # Convert to float
            if 'time' in item:
                time = float(item['time'])  # Convert to float
            if 'waiting_time' in item:
                waiting_time = float(item['waiting_time'])  # Convert to float
            if 'day_of_week' in item:
                days_of_week = item['day_of_week']

        print("distance", distance)
        print("time", time)
        print("days_of_week", days_of_week)
        print("waiting_time", waiting_time)
        price = calculate_price(distance, time, waiting_time, days_of_week)

        # Include 'price' in the context dictionary
        context = {'price': price}

        # Pass the context to the render function
        return render(request, 'custom.html', context)

    # Handle other HTTP methods or return an appropriate response
    return render(request, 'custom.html')


# def your_root_view(request):
#     return HttpResponse("Welcome to the pricing module!")


