import os
import csv

class CarBase:
    car_type        = None
    brand           = None
    photo_file_name = ''
    carrying        = 0
    
#     def __new__(cls, brand, photo_file_name, carrying):
#         if (brand == '') or (cls.get_photo_file_ext() == '') or (carrying == ''):
#             return
#         else:
#             if  (cls.get_photo_file_ext() == '.jpg')  and \
#                 (cls.get_photo_file_ext() == '.jpeg') and \
#                 (cls.get_photo_file_ext() == '.png' ) and \
#                 (cls.get_photo_file_ext() == '.gif'):
#                     return super(CarBase, cls).__new__(brand, photo_file_name, carrying)
#             else:
#                 return
               
    
    def __init__(self, brand, photo_file_name, carrying):
        self.brand           = brand
        self.photo_file_name = photo_file_name
        self.carrying        = float(carrying)
        
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]
        

class Car(CarBase):
    car_type              = 'car'
    passenger_seats_count = None
    
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):   
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type    = 'truck'
    body_width  = 0.
    body_height = 0.
    body_length = 0.
    
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        body_whl    = body_whl.split('x')
        if len(body_whl) == 3:
            try:
                self.body_width  = float(body_whl[1])
                self.body_height = float(body_whl[2])
                self.body_length = float(body_whl[0])
            except (ValueError):
                print('Not Valid')
        else:
            print('Not Valid')
        
    def get_body_volume(self):
        try:
            volume = self.body_width*self.body_height*self.body_length
        except ValueError:
            print('Not Valid')
        return volume


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    extra    = None
    
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

def get_car_list(csv_filename):
    car_list = []
    
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        try:
            next(reader)
        except:
            print('Empty file')
        
        for row in reader:
            if len(row) == 0:
                continue

            if  (os.path.splitext(row[3])[1] == '.jpg')  or \
                (os.path.splitext(row[3])[1] == '.jpeg') or \
                (os.path.splitext(row[3])[1] == '.png' ) or \
                (os.path.splitext(row[3])[1] == '.gif'):
                if row[0] == 'car':
                    if not(row[1] == '') and not(row[2] == '') and not(row[3] == '') and not(row[5] == ''):
                        car   =   Car(row[1],row[3],row[5],row[2])
                        car_list.append(car)
                
                if row[0] == 'truck':
                    if not(row[1] == '') and not(row[3] == '') and not(row[5] == ''):
                        truck = Truck(row[1],row[3],row[5],row[4])
                        car_list.append(truck)
                
                if row[0] == 'spec_machine':
                    if not(row[1] == '') and not(row[3] == '') and not(row[5] == '') and not(row[6] == ''):
                        spec  = SpecMachine(row[1],row[3],row[5],row[6])
                        car_list.append(spec)
                
            else:
                pass
            
    return car_list