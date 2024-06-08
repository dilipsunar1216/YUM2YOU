from app import create_app, db
from app.models import Train, Station, Vendor

app = create_app()
with app.app_context():
    db.create_all()

    # Add sample data for CST Mumbai to Gorakhpur
    train1 = Train(name="CST Mumbai to Gorakhpur", route="CST Mumbai-Gorakhpur")
    db.session.add(train1)
    db.session.commit()

    stations = [
        {"name": "CST Mumbai", "arrival_time": "06:00", "departure_time": "06:30"},
        {"name": "Thane", "arrival_time": "07:00", "departure_time": "07:05"},
        {"name": "Kalyan", "arrival_time": "07:30", "departure_time": "07:35"},
        {"name": "Igatpuri", "arrival_time": "09:00", "departure_time": "09:05"},
        {"name": "Nasik Road", "arrival_time": "10:00", "departure_time": "10:10"},
        {"name": "Manmad", "arrival_time": "11:00", "departure_time": "11:05"},
        {"name": "Bhusaval", "arrival_time": "13:00", "departure_time": "13:10"},
        {"name": "Itarsi", "arrival_time": "16:00", "departure_time": "16:15"},
        {"name": "Jabalpur", "arrival_time": "19:00", "departure_time": "19:15"},
        {"name": "Katni", "arrival_time": "20:00", "departure_time": "20:05"},
        {"name": "Satna", "arrival_time": "21:00", "departure_time": "21:05"},
        {"name": "Allahabad", "arrival_time": "23:00", "departure_time": "23:10"},
        {"name": "Varanasi", "arrival_time": "01:00", "departure_time": "01:15"},
        {"name": "Mau", "arrival_time": "03:00", "departure_time": "03:10"},
        {"name": "Gorakhpur", "arrival_time": "06:00", "departure_time": "End of Journey"}
    ]

    for station in stations:
        new_station = Station(train_id=train1.id, name=station['name'], arrival_time=station['arrival_time'], departure_time=station['departure_time'])
        db.session.add(new_station)
        db.session.commit()

        vendors = [
            {"name": f"{station['name']} Vendor 1", "description": "Delicious local cuisine", "image_url": "placeholder.png", "menu": '{"items": [{"name": "Item 1", "price": "100"}, {"name": "Item 2", "price": "150"}]}', "contact_info": "Contact details here"},
            {"name": f"{station['name']} Vendor 2", "description": "Tasty fast food", "image_url": "placeholder.png", "menu": '{"items": [{"name": "Item 3", "price": "120"}, {"name": "Item 4", "price": "180"}]}', "contact_info": "Contact details here"}
        ]

        for vendor in vendors:
            new_vendor = Vendor(station_id=new_station.id, name=vendor['name'], description=vendor['description'], image_url=vendor['image_url'], menu=vendor['menu'], contact_info=vendor['contact_info'])
            db.session.add(new_vendor)
            db.session.commit()
