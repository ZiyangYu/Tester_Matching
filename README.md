# Tester_Matching

A simple matching program created by Ziyang Yu for Applause

## Prerequisites

This program will run in python 3.
 Please make sure the virson of python 3 is currently being used on your machine

## Running the Test Matcher

On Mac:

In terminal, move into the directory of the program

In the directory of the program, run:

```
python ./main.py
```

After the welcome message, please enter the country code for the criteria, then hit Enter key

#### For a single country, please type the country code: US or JP or GB
```
US
```

#### For multiple countries, please seperate country code by "," only, no space in between:
```
US,JP
```

#### For all countries, please type:
```
ALL
```

After the country criteria, please list the criteria for device(s)

#### For a single device, please type the device description eg: iPhone 4
```
iPhone 4
```

#### For multiple countries, please seperate devices by "," only, no space in between devices:
```
iPhone 5,HTC One
```

After all the criterias are logged, the program will return the result.

## Testing Result

With one country, multiple devices:

```
$ python ./main.py
 
*****************Test Matcher*******************
 
Welcome!
Please input a list of Countries or ALL for Test Results, Split with comma with no space ",": 
US
 
Please input a list of devices for Test Results, Split with comma with no space ",": 
iPhone 4,HTC One
 
==================================================
Results: 
 
Total number of bugs that match with given criteria: 

106
 
Result with Experiences : 
Taybin Rutkin => 66
Miguel Bautista => 23
Michael Lubavin => 17
Leonard Sutton => 0
Mingquan Zheng => 0
Stanley Chen => 0
Lucas Lowry => 0
Sean Wellington => 0
Darshini Thiagarajan => 0
 
************************************************
```


With multiple country, multiple devices:

```
$ python ./main.py
 
*****************Test Matcher*******************
 
Welcome!
Please input a list of Countries or ALL for Test Results, Split with comma with no space ",": 
US,JP
 
Please input a list of devices for Test Results, Split with comma with no space ",": 
iPhone 4,HTC One
 
==================================================
Results: 
 
Total number of bugs that match with given criteria: 

172
 
Result with Experiences : 
Taybin Rutkin => 66
Sean Wellington => 45
Miguel Bautista => 23
Mingquan Zheng => 21
Michael Lubavin => 17
Leonard Sutton => 0
Stanley Chen => 0
Lucas Lowry => 0
Darshini Thiagarajan => 0
 
************************************************

```

with ALL country, one device:
```
$ python ./main.py
 
*****************Test Matcher*******************
 
Welcome!
Please input a list of Countries or ALL for Test Results, Split with comma with no space ",": 
ALL
 
Please input a list of devices for Test Results, Split with comma with no space ",": 
Nexus 4
 
==================================================
Results: 
 
Total number of bugs that match with given criteria: 

127
 
Result with Experiences : 
Darshini Thiagarajan => 28
Leonard Sutton => 27
Lucas Lowry => 25
Sean Wellington => 23
Mingquan Zheng => 13
Michael Lubavin => 11
Miguel Bautista => 0
Taybin Rutkin => 0
Stanley Chen => 0
 
************************************************

```

