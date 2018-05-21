# Company org

Given a list of employees and their direct manager, print out the company org chart.

## Example

### Input:

**Employee Name, Manager Name, Position, Year Hired**

Karl,Nancy,Manager,2009
Adam,Karl,Technician,2010
Bob,Karl,Technician,2012
John, Adam, Apprentice,2012
Cathy,Wendy,Manager,2013
Nancy,NULL,CEO,2007
Wendy,Nancy,Technician,2012

### Output:

Nancy (CEO) 2007
-Karl (Manager) 2009
--Adam (Technician) 2010
---John (Apprentice) 2012
--Bob (Technician) 2012
-Wendy (Manager) 2012
—-Cathy (Technician) 2013

## Run the program

In the folder run the command:

```
python company-org.py
```
