USE BaksoLoncat
GO
-- Insert MsSupplier Dummy Data
INSERT INTO MsSupplier
	(SupplierId,SupplierName,SupplierPhoneNumber,SupplierAddress,SupplierGender,SupplierDOB,SupplierEmail)
VALUES(
	'SP001','Jonathan Mulia','0877477777','Malibu Street No.35 Street','Male','1995-03-15','jona.mulia@gmail.com')
INSERT INTO MsSupplier
	(SupplierId,SupplierName,SupplierPhoneNumber,SupplierAddress,SupplierGender,SupplierDOB,SupplierEmail)
VALUES(
	'SP002','Elbert','0877889900','Kemenangan Street No.19 Street','Male','1990-01-01','ewijaya.1888@yahoo.co.id')
INSERT INTO MsSupplier
	(SupplierId,SupplierName,SupplierPhoneNumber,SupplierAddress,SupplierGender,SupplierDOB,SupplierEmail)
VALUES(
	'SP003','Kevinka','0877337722','Pademangan Street No.99 Street','Female','1995-10-10','kvkamine@gmail.com')
INSERT INTO MsSupplier
	(SupplierId,SupplierName,SupplierPhoneNumber,SupplierAddress,SupplierGender,SupplierDOB,SupplierEmail)
VALUES(
	'SP004','Patrick','0878700800','Cempaka Baru Street No. 80 Street','Male','1989-08-17','ptrickkk@gmail.com')
INSERT INTO MsSupplier
	(SupplierId,SupplierName,SupplierPhoneNumber,SupplierAddress,SupplierGender,SupplierDOB,SupplierEmail)
VALUES(
	'SP005','Sharon','0878888889','Kemerdekaan Street No. 45 Street','Female','2000-12-31','shrrniwj@yahoo.co.id')
INSERT INTO MsSupplier
	(SupplierId,SupplierName,SupplierPhoneNumber,SupplierAddress,SupplierGender,SupplierDOB,SupplierEmail)
VALUES(
	'SP006','Nicholas	','0878166482','Bungur Street No. 69 Street','Male','1996-11-03','nicho1010@yahoo.co.id')
INSERT INTO MsSupplier
	(SupplierId,SupplierName,SupplierPhoneNumber,SupplierAddress,SupplierGender,SupplierDOB,SupplierEmail)
VALUES(
	'SP007','Loganz','0813100477','Kuningan Street No. 199 Street','Male','1992-11-01','lggnz111@gmail.com')
INSERT INTO MsSupplier
	(SupplierId,SupplierName,SupplierPhoneNumber,SupplierAddress,SupplierGender,SupplierDOB,SupplierEmail)
VALUES(
	'SP008','Rizkia','0816899666','Kemanggisan Street No. 188 Street','Female','1992-02-29','rzkia229@gmail.com')
INSERT INTO MsSupplier
	(SupplierId,SupplierName,SupplierPhoneNumber,SupplierAddress,SupplierGender,SupplierDOB,SupplierEmail)
VALUES(
	'SP009','Ramayana','0857002884','Syahdan Street No. 7 Street','Female','1985-04-21','yana.rama@yahoo.co.id')
INSERT INTO MsSupplier
	(SupplierId,SupplierName,SupplierPhoneNumber,SupplierAddress,SupplierGender,SupplierDOB,SupplierEmail)
VALUES(
	'SP010','Sugiono','0811323567','Kijang Street No. 12 Street','Male','1993-10-11','kakegiono@yahoo.co.id')


-- Insert MsCustomer Dummy Data 
INSERT INTO MsCustomer
	(CustomerId,CustomerName,CustomerPhoneNumber,CustomerAddress,CustomerGender,CustomerEmail,CustomerDOB)
VALUES
	('CT001','Indran Kuntiz','0877184818','Walan Street No.77 Street','Male','indran.kuntiz@gmail.com','1999-10-31')
INSERT INTO MsCustomer
	(CustomerId,CustomerName,CustomerPhoneNumber,CustomerAddress,CustomerGender,CustomerEmail,CustomerDOB)
VALUES
	('CT002','Rajabasa','0828000034','Galag Street No.72 Street','Male','r.basa@gmail.com','1984-11-11')
INSERT INTO MsCustomer
	(CustomerId,CustomerName,CustomerPhoneNumber,CustomerAddress,CustomerGender,CustomerEmail,CustomerDOB)
VALUES
	('CT003','Mikhaya','0870200466','Hubi Street No.21 Street','Female','mimikhaya@gmail.com','1984-02-14')
INSERT INTO MsCustomer
	(CustomerId,CustomerName,CustomerPhoneNumber,CustomerAddress,CustomerGender,CustomerEmail,CustomerDOB)
VALUES
	('CT004','Jamalludin','0817455573','Wasanta Street No.35 Street','Male','jamal.ll4@gmail.com','1994-04-06')
INSERT INTO MsCustomer
	(CustomerId,CustomerName,CustomerPhoneNumber,CustomerAddress,CustomerGender,CustomerEmail,CustomerDOB)
VALUES
	('CT005','Olivia','0847184876','Jisha Street No.183 Street','Female','olivia.hera@gmail.com','2000-03-03')
INSERT INTO MsCustomer
	(CustomerId,CustomerName,CustomerPhoneNumber,CustomerAddress,CustomerGender,CustomerEmail,CustomerDOB)
VALUES
	('CT006','Rismayati','0821446691','Tritona Street No.7 Street','Female','rsmayati22@gmail.com','1998-02-22')
INSERT INTO MsCustomer
	(CustomerId,CustomerName,CustomerPhoneNumber,CustomerAddress,CustomerGender,CustomerEmail,CustomerDOB)
VALUES
	('CT007','Melati','0811200841','Bunga Street No.16 Street','Female','melamela.ti@gmail.com','1987-01-01')
INSERT INTO MsCustomer
	(CustomerId,CustomerName,CustomerPhoneNumber,CustomerAddress,CustomerGender,CustomerEmail,CustomerDOB)
VALUES
	('CT008','Aditya','0878727766','Kurnia Street No.202 Street','Male','aditya_mahendra@yahoo.co.id','1997-05-13')
INSERT INTO MsCustomer
	(CustomerId,CustomerName,CustomerPhoneNumber,CustomerAddress,CustomerGender,CustomerEmail,CustomerDOB)
VALUES
	('CT009','Shabira','0835193963','Alana Street No.139 Street','Female','bira.shaa@yahoo.co.id','1991-12-01')
INSERT INTO MsCustomer
	(CustomerId,CustomerName,CustomerPhoneNumber,CustomerAddress,CustomerGender,CustomerEmail,CustomerDOB)
VALUES
	('CT010','Krafatos','0825480491','Grishela Street No.33 Street','Male','kratos.fatos771@gmail.com','1997-07-01')

-- Insert MsStaff Dummy Data  
INSERT INTO MsStaff
	(StaffId,StaffName,StaffPhoneNumber,StaffAddress,StaffGender,StaffDOB,StaffEmail)
VALUES
	('SF001','Adhyastha','0888123888','Gunadarma Street No. 44 Street','Male','2001-01-02','adhyastha@gmail.com')
INSERT INTO MsStaff
	(StaffId,StaffName,StaffPhoneNumber,StaffAddress,StaffGender,StaffDOB,StaffEmail)
VALUES
	('SF002','Alaric','0811657928','Sukarnon Street No.1 Street','Male','1977-12-21','al.ricky@yahoo.co.id')
INSERT INTO MsStaff
	(StaffId,StaffName,StaffPhoneNumber,StaffAddress,StaffGender,StaffDOB,StaffEmail)
VALUES
	('SF003','Bagasan','0827969697','Granad Street No. 84 Street','Male','1999-07-24','bukanbagas31@gmail.com')
INSERT INTO MsStaff
	(StaffId,StaffName,StaffPhoneNumber,StaffAddress,StaffGender,StaffDOB,StaffEmail)
VALUES
	('SF004','Hyugan','0845666718','Padjadjaran Street No. 174 Street','Male','1988-09-04','not.neji@yahoo.co.id')
INSERT INTO MsStaff
	(StaffId,StaffName,StaffPhoneNumber,StaffAddress,StaffGender,StaffDOB,StaffEmail)
VALUES
	('SF005','Gibran','0817170845','Rakabuming Street No. 1 Street','Male','1995-11-23','gibran.lalala@gmail.com')
INSERT INTO MsStaff
	(StaffId,StaffName,StaffPhoneNumber,StaffAddress,StaffGender,StaffDOB,StaffEmail)
VALUES
	('SF006','Keandra','0822101112','Anggrek Street No. 26 Street','Male','1984-01-06','kea.ndra84@yahoo.co.id')
INSERT INTO MsStaff
	(StaffId,StaffName,StaffPhoneNumber,StaffAddress,StaffGender,StaffDOB,StaffEmail)
VALUES
	('SF007','Audrey','0813307299','Natasha Street No. 54 Street','Female','1984-06-01','adrey1684@yahoo.co.id')
INSERT INTO MsStaff
	(StaffId,StaffName,StaffPhoneNumber,StaffAddress,StaffGender,StaffDOB,StaffEmail)
VALUES
	('SF008','Claristha','0817470870','Haji Nawi Street No. 38 Street','Female','1994-03-19','clclhaha@gmail.com')
INSERT INTO MsStaff
	(StaffId,StaffName,StaffPhoneNumber,StaffAddress,StaffGender,StaffDOB,StaffEmail)
VALUES
	('SF009','Emilya','0828277701','Cipayung Street No. 123 Street','Female','1994-04-03','emil.karnda@gmail.com')
INSERT INTO MsStaff
	(StaffId,StaffName,StaffPhoneNumber,StaffAddress,StaffGender,StaffDOB,StaffEmail)
VALUES
	('SF010','Kumara','0816833773','Dewi Street No. 8 Street','Female','1979-06-27','kmara27@yahoo.co.id')

-- Insert MsMeatball Dummy Data
INSERT INTO MsMeatball
	(MeatballId,MeatballName,MeatballPrice)
VALUES
	('MB001','Bakso Sapi',11000)
INSERT INTO MsMeatball
	(MeatballId,MeatballName,MeatballPrice)
VALUES	
	('MB002','Fish Ball',13000)
INSERT INTO MsMeatball
	(MeatballId,MeatballName,MeatballPrice)
VALUES	
	('MB003','Swedish Meatball',10000)
INSERT INTO MsMeatball
	(MeatballId,MeatballName,MeatballPrice)
VALUES	
	('MB004','Pork Ball',38000)
INSERT INTO MsMeatball
	(MeatballId,MeatballName,MeatballPrice)
VALUES	
	('MB005','Tsukune',28500)
INSERT INTO MsMeatball
	(MeatballId,MeatballName,MeatballPrice)
VALUES	
	('MB006','Cocktail',22000)
INSERT INTO MsMeatball
	(MeatballId,MeatballName,MeatballPrice)
VALUES	
	('MB007','Bitterballen',12500)
INSERT INTO MsMeatball
	(MeatballId,MeatballName,MeatballPrice)
VALUES	
	('MB008','Kotbullar',15000)
INSERT INTO MsMeatball
	(MeatballId,MeatballName,MeatballPrice)
VALUES	
	('MB009','Pentol',16000)
INSERT INTO MsMeatball
	(MeatballId,MeatballName,MeatballPrice)
VALUES	
	('MB010','Cilok Premium',13000)

-- Insert MsIngredient Dummy Data
INSERT INTO MsIngredient
	(IngredientId,IngredientName,IngredientPrice)
VALUES
    ('IG001','Seledri',5500)
INSERT INTO MsIngredient
	(IngredientId,IngredientName,IngredientPrice)
VALUES
    ('IG002','Cuka',8500)
INSERT INTO MsIngredient
	(IngredientId,IngredientName,IngredientPrice)
VALUES
    ('IG003','Chikuwa',14500)
INSERT INTO MsIngredient
	(IngredientId,IngredientName,IngredientPrice)
VALUES
    ('IG004','Udon',11000)
INSERT INTO MsIngredient
	(IngredientId,IngredientName,IngredientPrice)
VALUES
    ('IG005','Ginseng Leaves',17500)
INSERT INTO MsIngredient
	(IngredientId,IngredientName,IngredientPrice)
VALUES
    ('IG006','Beef Meatloaf',31500)
INSERT INTO MsIngredient
	(IngredientId,IngredientName,IngredientPrice)
VALUES
    ('IG007','Tahu sutra',19000)
INSERT INTO MsIngredient
	(IngredientId,IngredientName,IngredientPrice)
VALUES
    ('IG008','Kecap',9000)
INSERT INTO MsIngredient
	(IngredientId,IngredientName,IngredientPrice)
VALUES
    ('IG009','Wijen',8500)
INSERT INTO MsIngredient
	(IngredientId,IngredientName,IngredientPrice)
VALUES
    ('IG010','Minyak Zaitun',12000)

-- Insert MsRecipe Dummy Data
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB001','IG001',3)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB001','IG005',4)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB002','IG007',6)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB003','IG003',5)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB003','IG008',4)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB004','IG002',5)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB005','IG005',5)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB005','IG008',3)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB006','IG002',5)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB007','IG004',4)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB008','IG002',3)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB008','IG005',2)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB009','IG004',3)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB009','IG006',3)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB010','IG001',3)
INSERT INTO MsRecipe
	(MeatballId,IngredientId,IngredientQty)
VALUES
	('MB010','IG003',3)

-- Insert MsHeaderPurchaseTransaction Dummy Data
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT001','SF002','SP004','2017-03-01')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT002','SF001','SP003','2019-11-12')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT003','SF008','SP009','2016-11-30')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT004','SF001','SP010','2015-01-28')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT005','SF006','SP001','2018-09-04')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT006','SF009','SP007','2018-01-15')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT007','SF010','SP010','2019-10-10')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT008','SF008','SP002','2016-07-17')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT009','SF003','SP003','2015-12-29')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT010','SF001','SP003','2016-02-29')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT011','SF007','SP005','2018-04-09')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT012','SF009','SP009','2017-09-14')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT013','SF003','SP001','2017-12-25')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT014','SF010','SP010','2014-12-31')
INSERT INTO MsHeaderPurchaseTransaction
	(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
VALUES
	('PT015','SF007','SP001','2016-06-26')

-- Insert MsDetailPurchaseTransaction Dummy Data
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT001','IG002',5)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT001','IG004',1)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT001','IG005',1)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT002','IG002',2)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT002','IG007',10)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT003','IG008',1)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT004','IG005',1)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT004','IG001',15)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT004','IG009',2)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT005','IG001',7)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT006','IG010',1)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT006','IG009',1)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT007','IG008',15)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT007','IG006',3)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT007','IG001',1)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT008','IG001',1)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT009','IG005',1)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT010','IG009',1)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT010','IG010',5)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT011','IG001',3)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT011','IG006',5)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT015','IG003',2)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT012','IG006',1)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT013','IG008',6)
INSERT INTO MsDetailPurchaseTransaction
	(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
VALUES
	('PT014','IG010',7)

--Insert MsHeaderSalesTransaction Dummy Data
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST001','CT003','SF001','2018-03-11')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST002','CT009','SF002','2016-08-13')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST003','CT001','SF005','2015-12-17')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST004','CT002','SF004','2014-12-26')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST005','CT003','SF010','2017-06-13')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST006','CT005','SF002','2019-01-30')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST007','CT002','SF005','2020-01-03')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST008','CT008','SF003','2017-03-03')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST009','CT009','SF004','2018-04-25')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST010','CT007','SF004','2015-11-28')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST011','CT004','SF007','2017-08-19')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST012','CT006','SF006','2016-05-25')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST013','CT009','SF006','2015-01-01')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST014','CT002','SF008','2018-11-02')
INSERT INTO MsHeaderSalesTransaction
	(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
VALUES
	('ST015','CT010','SF008','2018-02-27')

-- Insert MsDetailSalesTransaction Dummy Data
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST001','MB001',8)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST001','MB003',18)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST002','MB006',13)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST002','MB002',7)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST002','MB008',11)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST003','MB004',6)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST003','MB006',9)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST003','MB010',7)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST004','MB001',12)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST004','MB002',11)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST004','MB003',3)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST004','MB009',8)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST005','MB002',12)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST005','MB005',13)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST005','MB008',10)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST006','MB002',3)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST007','MB004',11)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST008','MB001',13)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST009','MB006',12)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST010','MB005',3)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST011','MB005',14)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST012','MB010',14)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST013','MB002',15)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST014','MB008',16)
INSERT INTO MsDetailSalesTransaction
	(SalesTransactionId,MeatballId,SalesTransactionQty)
VALUES
	('ST014','MB010',2)