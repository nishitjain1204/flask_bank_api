import sqlite3

data = [
  {
    "acc_num": 409000611074,
    "Date": "29 Jun 17",
    "trans_details": "TRF FROM  Indiaforensic SERVICES",
    "val_date": "29 Jun 17",
    "withdrawal_amt": "",
    "dep_amt": "10,00,000.00",
    "bal_amt": "10,00,000.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "5 Jul 17",
    "trans_details": "TRF FROM  Indiaforensic SERVICES",
    "val_date": "5 Jul 17",
    "withdrawal_amt": "",
    "dep_amt": "10,00,000.00",
    "bal_amt": "20,00,000.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "18 Jul 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "18 Jul 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "25,00,000.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "1 Aug 17",
    "trans_details": "TRF FRM  Indiaforensic SERVICES",
    "val_date": "1 Aug 17",
    "withdrawal_amt": "",
    "dep_amt": "30,00,000.00",
    "bal_amt": "55,00,000.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "60,00,000.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "65,00,000.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "70,00,000.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "75,00,000.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "80,00,000.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "85,00,000.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL01071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "1,33,900.00",
    "dep_amt": "",
    "bal_amt": "83,66,100.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL02071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "18,000.00",
    "dep_amt": "",
    "bal_amt": "83,48,100.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL03071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "5,000.00",
    "dep_amt": "",
    "bal_amt": "83,43,100.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL04071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "1,95,800.00",
    "dep_amt": "",
    "bal_amt": "81,47,300.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL05071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "81,600.00",
    "dep_amt": "",
    "bal_amt": "80,65,700.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL06071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "41,800.00",
    "dep_amt": "",
    "bal_amt": "80,23,900.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL07071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "98,500.00",
    "dep_amt": "",
    "bal_amt": "79,25,400.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL10071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "1,43,800.00",
    "dep_amt": "",
    "bal_amt": "77,81,600.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL11071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "3,31,650.00",
    "dep_amt": "",
    "bal_amt": "74,49,950.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL12071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "1,29,000.00",
    "dep_amt": "",
    "bal_amt": "73,20,950.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL13071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "2,30,013.00",
    "dep_amt": "",
    "bal_amt": "70,90,937.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL14071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "3,67,900.00",
    "dep_amt": "",
    "bal_amt": "67,23,037.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL15071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "1,08,000.00",
    "dep_amt": "",
    "bal_amt": "66,15,037.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL16071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "64,800.00",
    "dep_amt": "",
    "bal_amt": "65,50,237.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL17071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "1,41,000.00",
    "dep_amt": "",
    "bal_amt": "64,09,237.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL18071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "61,750.00",
    "dep_amt": "",
    "bal_amt": "63,47,487.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL19071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "67,920.00",
    "dep_amt": "",
    "bal_amt": "62,79,567.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL20071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "78,100.00",
    "dep_amt": "",
    "bal_amt": "62,01,467.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL21071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "35,650.00",
    "dep_amt": "",
    "bal_amt": "61,65,817.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL22071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "2,06,000.00",
    "dep_amt": "",
    "bal_amt": "59,59,817.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL24071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "35,300.00",
    "dep_amt": "",
    "bal_amt": "59,24,517.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL25071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "49,800.00",
    "dep_amt": "",
    "bal_amt": "58,74,717.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL26071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "53,000.00",
    "dep_amt": "",
    "bal_amt": "58,21,717.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL27071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "91,300.00",
    "dep_amt": "",
    "bal_amt": "57,30,417.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL28071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "57,499.00",
    "dep_amt": "",
    "bal_amt": "56,72,918.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL30071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "20,000.00",
    "dep_amt": "",
    "bal_amt": "56,52,918.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Aug 17",
    "trans_details": "INDO GIBL Indiaforensic STL31071",
    "val_date": "16 Aug 17",
    "withdrawal_amt": "19,400.00",
    "dep_amt": "",
    "bal_amt": "56,33,518.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL01081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "40,500.00",
    "dep_amt": "",
    "bal_amt": "55,93,018.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL02081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "2,42,300.00",
    "dep_amt": "",
    "bal_amt": "53,50,718.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL03081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "90,100.00",
    "dep_amt": "",
    "bal_amt": "52,60,618.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL04081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "1,13,250.00",
    "dep_amt": "",
    "bal_amt": "51,47,368.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL05081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "12,500.00",
    "dep_amt": "",
    "bal_amt": "51,34,868.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL06081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "40,000.00",
    "dep_amt": "",
    "bal_amt": "50,94,868.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL07081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "2,06,900.00",
    "dep_amt": "",
    "bal_amt": "48,87,968.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL08081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "2,76,000.00",
    "dep_amt": "",
    "bal_amt": "46,11,968.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL09081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "1,71,000.00",
    "dep_amt": "",
    "bal_amt": "44,40,968.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL10081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "40,100.00",
    "dep_amt": "",
    "bal_amt": "44,00,868.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL11081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "1,89,800.00",
    "dep_amt": "",
    "bal_amt": "42,11,068.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL12081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "55,800.00",
    "dep_amt": "",
    "bal_amt": "41,55,268.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL13081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "95,400.00",
    "dep_amt": "",
    "bal_amt": "40,59,868.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL14081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "2,71,323.00",
    "dep_amt": "",
    "bal_amt": "37,88,545.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL16081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "2,00,600.00",
    "dep_amt": "",
    "bal_amt": "35,87,945.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL17081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "1,76,900.00",
    "dep_amt": "",
    "bal_amt": "34,11,045.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL18081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "1,50,050.00",
    "dep_amt": "",
    "bal_amt": "32,60,995.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL19081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "82,500.00",
    "dep_amt": "",
    "bal_amt": "31,78,495.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL20081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "14,800.00",
    "dep_amt": "",
    "bal_amt": "31,63,695.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL21081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "1,50,600.00",
    "dep_amt": "",
    "bal_amt": "30,13,095.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL22081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "2,03,325.00",
    "dep_amt": "",
    "bal_amt": "28,09,770.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL23081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "1,23,900.00",
    "dep_amt": "",
    "bal_amt": "26,85,870.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL24081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "33,863.00",
    "dep_amt": "",
    "bal_amt": "26,52,007.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL25081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "32,000.00",
    "dep_amt": "",
    "bal_amt": "26,20,007.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL26081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "8,299.00",
    "dep_amt": "",
    "bal_amt": "26,11,708.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL28081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "52,219.00",
    "dep_amt": "",
    "bal_amt": "25,59,489.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL29081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "96,450.00",
    "dep_amt": "",
    "bal_amt": "24,63,039.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL30081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "1,39,863.00",
    "dep_amt": "",
    "bal_amt": "23,23,176.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL31081",
    "val_date": "6 Sep 17",
    "withdrawal_amt": "52,723.00",
    "dep_amt": "",
    "bal_amt": "22,70,453.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL01091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "77,251.00",
    "dep_amt": "",
    "bal_amt": "21,93,202.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL02091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "20,000.00",
    "dep_amt": "",
    "bal_amt": "21,73,202.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL03091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "10,000.00",
    "dep_amt": "",
    "bal_amt": "21,63,202.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL04091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "1,03,600.00",
    "dep_amt": "",
    "bal_amt": "20,59,602.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL05091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "71,000.00",
    "dep_amt": "",
    "bal_amt": "19,88,602.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL06091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "1,29,400.00",
    "dep_amt": "",
    "bal_amt": "18,59,202.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL07091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "2,90,163.00",
    "dep_amt": "",
    "bal_amt": "15,69,039.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL08091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "34,300.00",
    "dep_amt": "",
    "bal_amt": "15,34,739.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL09091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "49,800.00",
    "dep_amt": "",
    "bal_amt": "14,84,939.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL10091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "44,800.00",
    "dep_amt": "",
    "bal_amt": "14,40,139.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL11091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "1,51,550.00",
    "dep_amt": "",
    "bal_amt": "12,88,589.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL12091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "3,10,399.00",
    "dep_amt": "",
    "bal_amt": "9,78,190.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL13091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "2,71,401.00",
    "dep_amt": "",
    "bal_amt": "7,06,789.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL14091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "2,75,449.00",
    "dep_amt": "",
    "bal_amt": "4,31,340.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL15091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "51,502.00",
    "dep_amt": "",
    "bal_amt": "3,79,838.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL16091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "36,650.00",
    "dep_amt": "",
    "bal_amt": "3,43,188.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL17091",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "99,600.00",
    "dep_amt": "",
    "bal_amt": "2,43,588.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "7,43,588.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "12,43,588.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "17,43,588.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "22,43,588.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Sep 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "25 Sep 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "27,43,588.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "26 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL18091",
    "val_date": "26 Sep 17",
    "withdrawal_amt": "4,11,763.00",
    "dep_amt": "",
    "bal_amt": "23,31,825.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "26 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL19091",
    "val_date": "26 Sep 17",
    "withdrawal_amt": "3,55,138.00",
    "dep_amt": "",
    "bal_amt": "19,76,687.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "26 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL20091",
    "val_date": "26 Sep 17",
    "withdrawal_amt": "88,656.00",
    "dep_amt": "",
    "bal_amt": "18,88,031.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "26 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL21091",
    "val_date": "26 Sep 17",
    "withdrawal_amt": "14,800.00",
    "dep_amt": "",
    "bal_amt": "18,73,231.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "26 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL22091",
    "val_date": "26 Sep 17",
    "withdrawal_amt": "27,000.00",
    "dep_amt": "",
    "bal_amt": "18,46,231.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "26 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL23091",
    "val_date": "26 Sep 17",
    "withdrawal_amt": "42,850.00",
    "dep_amt": "",
    "bal_amt": "18,03,381.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "26 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL24091",
    "val_date": "26 Sep 17",
    "withdrawal_amt": "39,925.00",
    "dep_amt": "",
    "bal_amt": "17,63,456.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "26 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL25091",
    "val_date": "26 Sep 17",
    "withdrawal_amt": "2,02,106.00",
    "dep_amt": "",
    "bal_amt": "15,61,350.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "27 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL26091",
    "val_date": "27 Sep 17",
    "withdrawal_amt": "1,69,802.00",
    "dep_amt": "",
    "bal_amt": "13,91,548.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "28 Sep 17",
    "trans_details": "INDO GIBL Indiaforensic STL27091",
    "val_date": "28 Sep 17",
    "withdrawal_amt": "2,00,570.00",
    "dep_amt": "",
    "bal_amt": "11,90,978.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "3 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL28091",
    "val_date": "3 Oct 17",
    "withdrawal_amt": "12,106.00",
    "dep_amt": "",
    "bal_amt": "11,78,872.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "3 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL29091",
    "val_date": "3 Oct 17",
    "withdrawal_amt": "12,611.00",
    "dep_amt": "",
    "bal_amt": "11,66,261.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "3 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL30091",
    "val_date": "3 Oct 17",
    "withdrawal_amt": "9,375.00",
    "dep_amt": "",
    "bal_amt": "11,56,886.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "4 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL03101",
    "val_date": "4 Oct 17",
    "withdrawal_amt": "1,25,200.00",
    "dep_amt": "",
    "bal_amt": "10,31,686.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "5 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL04101",
    "val_date": "5 Oct 17",
    "withdrawal_amt": "61,400.00",
    "dep_amt": "",
    "bal_amt": "9,70,286.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL05101",
    "val_date": "6 Oct 17",
    "withdrawal_amt": "1,43,700.00",
    "dep_amt": "",
    "bal_amt": "8,26,586.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Oct 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "16 Oct 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "13,26,586.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Oct 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "16 Oct 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "18,26,586.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "16 Oct 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "16 Oct 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "23,26,586.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "17 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL06101",
    "val_date": "17 Oct 17",
    "withdrawal_amt": "6,000.00",
    "dep_amt": "",
    "bal_amt": "23,20,586.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "17 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL07101",
    "val_date": "17 Oct 17",
    "withdrawal_amt": "97,950.00",
    "dep_amt": "",
    "bal_amt": "22,22,636.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "17 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL08101",
    "val_date": "17 Oct 17",
    "withdrawal_amt": "33,000.00",
    "dep_amt": "",
    "bal_amt": "21,89,636.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "17 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL09101",
    "val_date": "17 Oct 17",
    "withdrawal_amt": "3,29,300.00",
    "dep_amt": "",
    "bal_amt": "18,60,336.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "17 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL10101",
    "val_date": "17 Oct 17",
    "withdrawal_amt": "18,000.00",
    "dep_amt": "",
    "bal_amt": "18,42,336.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "17 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL11101",
    "val_date": "17 Oct 17",
    "withdrawal_amt": "1,13,400.00",
    "dep_amt": "",
    "bal_amt": "17,28,936.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "17 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL12101",
    "val_date": "17 Oct 17",
    "withdrawal_amt": "2,62,226.00",
    "dep_amt": "",
    "bal_amt": "14,66,710.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "17 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL13101",
    "val_date": "17 Oct 17",
    "withdrawal_amt": "3,18,750.00",
    "dep_amt": "",
    "bal_amt": "11,47,960.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "17 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL14101",
    "val_date": "17 Oct 17",
    "withdrawal_amt": "65,549.00",
    "dep_amt": "",
    "bal_amt": "10,82,411.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "18 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL17101",
    "val_date": "18 Oct 17",
    "withdrawal_amt": "2,06,501.00",
    "dep_amt": "",
    "bal_amt": "8,75,910.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "21 Oct 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "21 Oct 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "13,75,910.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "21 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL18101",
    "val_date": "21 Oct 17",
    "withdrawal_amt": "85,000.00",
    "dep_amt": "",
    "bal_amt": "12,90,910.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "21 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL19101",
    "val_date": "21 Oct 17",
    "withdrawal_amt": "76,389.00",
    "dep_amt": "",
    "bal_amt": "12,14,521.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "21 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL20101",
    "val_date": "21 Oct 17",
    "withdrawal_amt": "62,725.00",
    "dep_amt": "",
    "bal_amt": "11,51,796.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "23 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL21101",
    "val_date": "23 Oct 17",
    "withdrawal_amt": "39,000.00",
    "dep_amt": "",
    "bal_amt": "11,12,796.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "23 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL22101",
    "val_date": "23 Oct 17",
    "withdrawal_amt": "9,600.00",
    "dep_amt": "",
    "bal_amt": "11,03,196.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "24 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL23101",
    "val_date": "24 Oct 17",
    "withdrawal_amt": "1,23,260.00",
    "dep_amt": "",
    "bal_amt": "9,79,936.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "25 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL24101",
    "val_date": "25 Oct 17",
    "withdrawal_amt": "3,69,803.00",
    "dep_amt": "",
    "bal_amt": "6,10,133.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "26 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL25101",
    "val_date": "26 Oct 17",
    "withdrawal_amt": "1,70,125.00",
    "dep_amt": "",
    "bal_amt": "4,40,008.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "26 Oct 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "26 Oct 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "9,40,008.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "27 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL26101",
    "val_date": "27 Oct 17",
    "withdrawal_amt": "2,08,000.00",
    "dep_amt": "",
    "bal_amt": "7,32,008.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "30 Oct 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "30 Oct 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "12,32,008.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "30 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL27101",
    "val_date": "30 Oct 17",
    "withdrawal_amt": "2,91,150.00",
    "dep_amt": "",
    "bal_amt": "9,40,858.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "30 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL28101",
    "val_date": "30 Oct 17",
    "withdrawal_amt": "24,000.00",
    "dep_amt": "",
    "bal_amt": "9,16,858.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "31 Oct 17",
    "trans_details": "INDO GIBL Indiaforensic STL30101",
    "val_date": "31 Oct 17",
    "withdrawal_amt": "1,41,546.00",
    "dep_amt": "",
    "bal_amt": "7,75,312.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "1 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL31101",
    "val_date": "1 Nov 17",
    "withdrawal_amt": "80,000.00",
    "dep_amt": "",
    "bal_amt": "6,95,312.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "2 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL01111",
    "val_date": "2 Nov 17",
    "withdrawal_amt": "46,250.00",
    "dep_amt": "",
    "bal_amt": "6,49,062.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "3 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL02111",
    "val_date": "3 Nov 17",
    "withdrawal_amt": "42,825.00",
    "dep_amt": "",
    "bal_amt": "6,06,237.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL03111",
    "val_date": "6 Nov 17",
    "withdrawal_amt": "1,79,463.00",
    "dep_amt": "",
    "bal_amt": "4,26,774.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL04111",
    "val_date": "6 Nov 17",
    "withdrawal_amt": "18,949.00",
    "dep_amt": "",
    "bal_amt": "4,07,825.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL05111",
    "val_date": "6 Nov 17",
    "withdrawal_amt": "91,441.00",
    "dep_amt": "",
    "bal_amt": "3,16,384.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "7 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL06111",
    "val_date": "7 Nov 17",
    "withdrawal_amt": "1,47,750.00",
    "dep_amt": "",
    "bal_amt": "1,68,634.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "8 Nov 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "8 Nov 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "6,68,634.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "8 Nov 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "8 Nov 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "11,68,634.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "8 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL07111",
    "val_date": "8 Nov 17",
    "withdrawal_amt": "1,10,188.00",
    "dep_amt": "",
    "bal_amt": "10,58,446.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "9 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL08111",
    "val_date": "9 Nov 17",
    "withdrawal_amt": "61,870.00",
    "dep_amt": "",
    "bal_amt": "9,96,576.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "10 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL09111",
    "val_date": "10 Nov 17",
    "withdrawal_amt": "84,101.00",
    "dep_amt": "",
    "bal_amt": "9,12,475.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "14 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL10111",
    "val_date": "14 Nov 17",
    "withdrawal_amt": "1,29,700.00",
    "dep_amt": "",
    "bal_amt": "7,82,775.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "14 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL11111",
    "val_date": "14 Nov 17",
    "withdrawal_amt": "7,499.00",
    "dep_amt": "",
    "bal_amt": "7,75,276.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "14 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL12111",
    "val_date": "14 Nov 17",
    "withdrawal_amt": "80,100.00",
    "dep_amt": "",
    "bal_amt": "6,95,176.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "14 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL13111",
    "val_date": "14 Nov 17",
    "withdrawal_amt": "1,43,850.00",
    "dep_amt": "",
    "bal_amt": "5,51,326.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "15 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL14111",
    "val_date": "15 Nov 17",
    "withdrawal_amt": "2,89,500.00",
    "dep_amt": "",
    "bal_amt": "2,61,826.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "17 Nov 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "17 Nov 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "7,61,826.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "17 Nov 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "17 Nov 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "12,61,826.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "17 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL16111",
    "val_date": "17 Nov 17",
    "withdrawal_amt": "94,900.00",
    "dep_amt": "",
    "bal_amt": "11,66,926.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "17 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL15111",
    "val_date": "17 Nov 17",
    "withdrawal_amt": "2,24,851.00",
    "dep_amt": "",
    "bal_amt": "9,42,075.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "18 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL17111",
    "val_date": "18 Nov 17",
    "withdrawal_amt": "2,84,953.00",
    "dep_amt": "",
    "bal_amt": "6,57,122.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "20 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL18111",
    "val_date": "20 Nov 17",
    "withdrawal_amt": "1,15,150.00",
    "dep_amt": "",
    "bal_amt": "5,41,972.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "20 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL19111",
    "val_date": "20 Nov 17",
    "withdrawal_amt": "40,000.00",
    "dep_amt": "",
    "bal_amt": "5,01,972.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "21 Nov 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "21 Nov 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "10,01,972.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "21 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL20111",
    "val_date": "21 Nov 17",
    "withdrawal_amt": "1,45,900.00",
    "dep_amt": "",
    "bal_amt": "8,56,072.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "22 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL21111",
    "val_date": "22 Nov 17",
    "withdrawal_amt": "83,251.00",
    "dep_amt": "",
    "bal_amt": "7,72,821.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "23 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL22111",
    "val_date": "23 Nov 17",
    "withdrawal_amt": "1,92,200.00",
    "dep_amt": "",
    "bal_amt": "5,80,621.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "24 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL23111",
    "val_date": "24 Nov 17",
    "withdrawal_amt": "74,799.00",
    "dep_amt": "",
    "bal_amt": "5,05,822.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "27 Nov 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "27 Nov 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "10,05,822.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "27 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL24117",
    "val_date": "27 Nov 17",
    "withdrawal_amt": "19,400.00",
    "dep_amt": "",
    "bal_amt": "9,86,422.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "27 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL25117",
    "val_date": "27 Nov 17",
    "withdrawal_amt": "39,700.00",
    "dep_amt": "",
    "bal_amt": "9,46,722.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "27 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL26117",
    "val_date": "27 Nov 17",
    "withdrawal_amt": "42,800.00",
    "dep_amt": "",
    "bal_amt": "9,03,922.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "28 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL27111",
    "val_date": "28 Nov 17",
    "withdrawal_amt": "1,00,402.00",
    "dep_amt": "",
    "bal_amt": "8,03,520.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "29 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL28111",
    "val_date": "29 Nov 17",
    "withdrawal_amt": "1,01,500.00",
    "dep_amt": "",
    "bal_amt": "7,02,020.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "30 Nov 17",
    "trans_details": "INDO GIBL Indiaforensic STL29111",
    "val_date": "30 Nov 17",
    "withdrawal_amt": "36,961.00",
    "dep_amt": "",
    "bal_amt": "6,65,059.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "2 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL30111",
    "val_date": "2 Dec 17",
    "withdrawal_amt": "67,850.00",
    "dep_amt": "",
    "bal_amt": "5,97,209.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "2 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL01121",
    "val_date": "2 Dec 17",
    "withdrawal_amt": "19,800.00",
    "dep_amt": "",
    "bal_amt": "5,77,409.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "4 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL02121",
    "val_date": "4 Dec 17",
    "withdrawal_amt": "10,000.00",
    "dep_amt": "",
    "bal_amt": "5,67,409.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "4 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL03121",
    "val_date": "4 Dec 17",
    "withdrawal_amt": "24,500.00",
    "dep_amt": "",
    "bal_amt": "5,42,909.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "5 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL04121",
    "val_date": "5 Dec 17",
    "withdrawal_amt": "41,700.00",
    "dep_amt": "",
    "bal_amt": "5,01,209.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Dec 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "6 Dec 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "10,01,209.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "6 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL05121",
    "val_date": "6 Dec 17",
    "withdrawal_amt": "2,18,050.00",
    "dep_amt": "",
    "bal_amt": "7,83,159.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "7 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL06121",
    "val_date": "7 Dec 17",
    "withdrawal_amt": "1,86,400.00",
    "dep_amt": "",
    "bal_amt": "5,96,759.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "8 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL07121",
    "val_date": "8 Dec 17",
    "withdrawal_amt": "1,71,330.00",
    "dep_amt": "",
    "bal_amt": "4,25,429.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "11 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL08121",
    "val_date": "11 Dec 17",
    "withdrawal_amt": "34,400.00",
    "dep_amt": "",
    "bal_amt": "3,91,029.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "11 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL09121",
    "val_date": "11 Dec 17",
    "withdrawal_amt": "51,199.00",
    "dep_amt": "",
    "bal_amt": "3,39,830.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "11 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL10121",
    "val_date": "11 Dec 17",
    "withdrawal_amt": "1,59,150.00",
    "dep_amt": "",
    "bal_amt": "1,80,680.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "12 Dec 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "12 Dec 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "6,80,680.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "12 Dec 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "12 Dec 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "11,80,680.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "13 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL11121",
    "val_date": "13 Dec 17",
    "withdrawal_amt": "2,06,075.00",
    "dep_amt": "",
    "bal_amt": "9,74,605.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "13 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL12121",
    "val_date": "13 Dec 17",
    "withdrawal_amt": "1,42,000.00",
    "dep_amt": "",
    "bal_amt": "8,32,605.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "14 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL13121",
    "val_date": "14 Dec 17",
    "withdrawal_amt": "3,50,350.00",
    "dep_amt": "",
    "bal_amt": "4,82,255.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "15 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL14121",
    "val_date": "15 Dec 17",
    "withdrawal_amt": "3,43,900.00",
    "dep_amt": "",
    "bal_amt": "1,38,355.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "18 Dec 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "18 Dec 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "6,38,355.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "18 Dec 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "18 Dec 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "11,38,355.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "18 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL15121",
    "val_date": "18 Dec 17",
    "withdrawal_amt": "2,10,500.00",
    "dep_amt": "",
    "bal_amt": "9,27,855.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "18 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL17121",
    "val_date": "18 Dec 17",
    "withdrawal_amt": "1,39,500.00",
    "dep_amt": "",
    "bal_amt": "7,88,355.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "18 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL16121",
    "val_date": "18 Dec 17",
    "withdrawal_amt": "92,550.00",
    "dep_amt": "",
    "bal_amt": "6,95,805.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "19 Dec 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "19 Dec 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "11,95,805.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "19 Dec 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "19 Dec 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "16,95,805.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "19 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL18121",
    "val_date": "19 Dec 17",
    "withdrawal_amt": "6,54,498.00",
    "dep_amt": "",
    "bal_amt": "10,41,307.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "20 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL19121",
    "val_date": "20 Dec 17",
    "withdrawal_amt": "5,04,450.00",
    "dep_amt": "",
    "bal_amt": "5,36,857.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "20 Dec 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "20 Dec 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "10,36,857.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "21 Dec 17",
    "trans_details": "INDO GIBL Indiaforensic STL20121",
    "val_date": "21 Dec 17",
    "withdrawal_amt": "5,61,225.00",
    "dep_amt": "",
    "bal_amt": "4,75,632.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "21 Dec 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "21 Dec 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "9,75,632.00"
  },
  {
    "acc_num": 409000611074,
    "Date": "21 Dec 17",
    "trans_details": "FDRL/INTERNAL FUND TRANSFE",
    "val_date": "21 Dec 17",
    "withdrawal_amt": "",
    "dep_amt": "5,00,000.00",
    "bal_amt": "14,75,632.00"
  }
]

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

# cursor.execute('''CREATE TABLE ACCOUNTS
               
#         (ID integer primary key autoincrement,
#             ACC_NUM  INTEGER,
#         DATE_ TEXT,
#         VALUE_DATE TEXT,
#         TRANS_DETAILS TEXT,
#         WITHDRAWAL_AMT TEXT,
#         DEPOSIT_AMT TEXT,
#         BALANCE_AMT TEXT
#         );''')

# for accounts in data :
#     cursor.execute(
        
#         f''' INSERT INTO ACCOUNTS(
            
#             ACC_NUM , DATE_ , TRANS_DETAILS , VALUE_DATE , WITHDRAWAL_AMT , DEPOSIT_AMT , BALANCE_AMT
            
#             )  
            
#             VALUES ({accounts.get("acc_num")} ,{accounts.get("Date")},{accounts.get( "trans_details")},{accounts.get("val_date")},{accounts.get("withdrawal_amt")},{accounts.get("dep_amt")},{accounts.get("bal_amt")} )'''
        
#     ) 

cursor.executemany("""
    INSERT INTO ACCOUNTS(
            
            ACC_NUM , DATE_ , TRANS_DETAILS , VALUE_DATE , WITHDRAWAL_AMT , DEPOSIT_AMT , BALANCE_AMT
            
            )  
    VALUES
        (:acc_num, :Date, :trans_details, :val_date, :withdrawal_amt , :dep_amt , :bal_amt)""", data)

conn.commit()
    


print("Records inserted........")

# Closing the connection
conn.close()