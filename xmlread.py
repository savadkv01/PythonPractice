
import xml.etree.ElementTree as ET
import pandas as pd

# Define the path to your XML file
xml_file_path = "D:\My Learning\PROJECTS\python_practice\BCDOverview.xml"

# Parse the XML file using ElementTree
try:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    # Initialize lists to store data
    data = []
    
    # Extract data from the XML and append to the data list
    data_list = []

    # Iterate through each PNR
    for pnr in root.findall('.//PNR'):
        record_locator = pnr.find("RecordLocator").text
        Client_Identifier = pnr.find("ClientIdentifier").text
        Global_CustomerNumber = pnr.find("GlobalCustomerNumber").text
        Customer_Number = pnr.find("CustomerNumber").text
        Booking_Date = pnr.find("BookingDate").text
        Last_Update = pnr.find("LastUpdate").text
        Ticketed_Ind = pnr.find("TicketedInd").text
        Ticketing_Date = pnr.find("TicketingDate").text
        Intl_Flight = pnr.find("IntlFlight").text
        GDS_Code = pnr.find("GDSCode").text
        Booking_PCC = pnr.find("BookingPCC").text
        Booking_Country = pnr.find("BookingCountry").text
        PNRStored_Fare = pnr.find("PNRStoredFare").text
        Currency_Code = pnr.find("CurrencyCode").text
        Cancelled_Ind = pnr.find("CancelledInd").text
        customer_num = pnr.find('.//CustomField[Name="CUSTOMER NUMBER"]/Value').text
        OBT_USAGE = pnr.find('.//CustomField[Name="OBT USAGE"]/Value').text
        EMPLOYEE_NUMBER_element = pnr.find('.//CustomField[Name="EMPLOYEE NUMBER"]/Value')
        EMPLOYEE_NUMBER = EMPLOYEE_NUMBER_element.text if EMPLOYEE_NUMBER_element is not None else None
        
        BOOKERS_NAME = pnr.find('.//CustomField[Name="BOOKERS NAME"]/Value').text
        
        AREA_DEPT_element = pnr.find('.//CustomField[Name="AREA/DEPT"]/Value')
        AREA_DEPT = AREA_DEPT_element.text if AREA_DEPT_element is not None else None
        
        COST_CODE_element = pnr.find('.//CustomField[Name="COST CODE NUMBER"]/Value')
        COST_CODE = COST_CODE_element.text if COST_CODE_element is not None else None
        
        Dept = pnr.find('.//CustomField[Name="DEPARTMENT"]/Value').text
        TRAVELER_STATUS_element = pnr.find('.//CustomField[Name="TRAVELER STATUS"]/Value')
        TRAVELER_STATUS = TRAVELER_STATUS_element.text if TRAVELER_STATUS_element is not None else None
        
        eqno_element = pnr.find('.//CustomField[Name="EQUIPMENT NUMBER"]/Value')
        eqno = eqno_element.text if eqno_element is not None else None
        

        reason_of_trip = pnr.find('.//CustomField[Name="REASON OF TRIP"]/Value').text

        traveler = pnr.find('.//TravelerList/Traveler')
        first_name = traveler.find('FirstName').text
        last_name = traveler.find('LastName').text
        email = traveler.find('EmailAddress').text
        Name_Reference = traveler.find('NameReference').text
        Traveler_ContactPhone = traveler.find('TravelerContactPhone').text
        Traveler_HomePhone = traveler.find('TravelerHomePhone').text
        Traveler_WorkPhone = traveler.find('TravelerWorkPhone').text
        Emergency_ContactName = traveler.find('EmergencyContactName').text
        Emergency_ContactPhone = traveler.find('EmergencyContactPhone').text

        segment_list = pnr.findall('.//SegmentList/AirSegment')
        for segment in segment_list:
            airline = segment.find('AirlineName').text
            Airline_Code= segment.find('AirlineCode').text
            flight_number = segment.find('FlightNumber').text
            St = segment.find('Seat').text
            Booking_Class = segment.find('BookingClass').text
            BookingClass_Description = segment.find('BookingClassDescription').text
            departure_iata = segment.find('DepartureIATACode').text
            Departure_AirportName = segment.find('DepartureAirportName').text
            Departure_CountryCode = segment.find('DepartureCountryCode').text
            Departure_CountryName = segment.find('DepartureCountryName').text
            Departure_DateTime = segment.find('DepartureDateTime').text

            arrival_iata = segment.find('ArrivalIATACode').text
            ArrivalAirportName = segment.find('ArrivalAirportName').text
            Arrival_CountryCode = segment.find('ArrivalCountryCode').text
            Arrival_CountryName = segment.find('ArrivalCountryName').text
            Arrival_DateTime = segment.find('ArrivalDateTime').text
            Segment_Number = segment.find('SegmentNumber').text
            Fare_Basis = segment.find('FareBasis').text
            Action_StatusCode = segment.find('ActionStatusCode').text
            miles = segment.find('Miles').text
            duration = segment.find('Duration').text

            data_list.append({
                'RecordLocator': record_locator,
                'ClientIdentifier': Client_Identifier,
                'GlobalCustomerNumber': Global_CustomerNumber,
                'CustomerNumber': Customer_Number,
                'BookingDate':Booking_Date,
                'LastUpdate':Last_Update,
                'TicketedInd':Ticketed_Ind,
                'TicketingDate':Ticketing_Date,
                'IntlFlight':Intl_Flight,
                'GDSCode':GDS_Code,
                'BookingPCC':Booking_PCC,
                'BookingCountry':Booking_Country,
                'PNRStoredFare':PNRStored_Fare,
                'CurrencyCode':Currency_Code,
                'CancelledInd':Cancelled_Ind,
                    
                'BookingDate': Booking_Date,
                'LastUpdate': Last_Update,
                'CUSTOMER NUMBER_Custom': customer_num,
                'REASON OF TRIP': reason_of_trip,
                'OBT USAGE':OBT_USAGE,
                'EMPLOYEE NUMBER':EMPLOYEE_NUMBER,
                'BOOKERS NAME':BOOKERS_NAME,
                'AREA/DEPT':AREA_DEPT,
                'COST CODE NUMBER':COST_CODE,
                'DEPARTMENT':Dept,
                'TRAVELER STATUS':TRAVELER_STATUS,
                'EQUIPMENT NUMBER': eqno,
                'First Name': first_name,
                'Last Name': last_name,
                'Email': email,
                'NameReference': Name_Reference,
                'TravelerContactPhone': Traveler_ContactPhone,
                'TravelerHomePhone': Traveler_HomePhone,
                'TravelerWorkPhone': Traveler_WorkPhone,
                'EmergencyContactName': Emergency_ContactName,
                'EmergencyContactPhone': Emergency_ContactPhone,
                'Airline': airline,
                'AirlineCode':Airline_Code,
                'Flight Number': flight_number,
                'Seat':St,
                'BookingClass':Booking_Class,
                'BookingClassDescription':BookingClass_Description,
                'Departure IATA': departure_iata,
                'DepartureAirportName':Departure_AirportName,
                'DepartureCountryCode':Departure_CountryCode,
                'DepartureCountryName':Departure_CountryName,
                'DepartureDateTime':Departure_DateTime,
                'Arrival IATA': arrival_iata,
                'ArrivalAirportName':ArrivalAirportName,
                'ArrivalCountryCode':Arrival_CountryCode,
                'ArrivalCountryName':Arrival_CountryName,
                'ArrivalDateTime':Arrival_DateTime,
                'SegmentNumber':Segment_Number,
                'FareBasis':Fare_Basis,
                'ActionStatusCode':Action_StatusCode,
                'Miles':miles,
                'Duration':duration
                
            })

    # Create a DataFrame
    df = pd.DataFrame(data_list)

    # Display the DataFrame
    print(df)
    
    # You can also save the DataFrame to a CSV or other format
    df.to_csv("output_table2.csv", index=False)
    
except ET.ParseError as e:
    print("XML parsing error:", e)
except FileNotFoundError:
    print("XML file not found")