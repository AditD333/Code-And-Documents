CREATE DATABASE BaksoLoncat
DROP DATABASE BaksoLoncat
GO
USE BaksoLoncat
GO

--Create Table MsSupplier
CREATE TABLE MsSupplier(
	SupplierId CHAR (5) PRIMARY KEY NOT NULL CHECK (SupplierId LIKE 'SP[0-9][0-9][0-9]'),
	SupplierName VARCHAR (50) NOT NULL CHECK (LEN(SupplierName) > 5),
	SupplierPhoneNumber VARCHAR (50) NOT NULL CHECK (SupplierPhoneNumber LIKE '08%'),
	SupplierAddress VARCHAR(100) NOT NULL CHECK (SupplierAddress LIKE '%Street'),
	SupplierGender VARCHAR (7) NOT NULL CHECK( SupplierGender IN ('Male','Female')),
	SupplierDOB DATE NOT NULL CHECK (DATEDIFF(YEAR,SupplierDOB,GETDATE()) > 17),
	SupplierEmail VARCHAR(100) NOT NULL CHECK (SupplierEmail LIKE '%@gmail.com' OR SupplierEmail LIKE '%@yahoo.co.id')
)

--Create Table MsCustomer
CREATE TABLE MsCustomer(
    CustomerId  CHAR (5) PRIMARY KEY NOT NULL CHECK (CustomerId LIKE 'CT[0-9][0-9][0-9]'),
    CustomerName VARCHAR (50) NOT NULL CHECK (LEN(CustomerName) > 5),
	CustomerPhoneNumber varchar(50) NOT NULL CHECK (CustomerPhoneNumber LIKE '08%'),
	CustomerAddress varchar(50) NOT NULL CHECK (CustomerAddress LIKE '%Street'),
    CustomerGender varchar(50) NOT NULL CHECK (CustomerGender IN ('Male','Female')),
    CustomerEmail varchar(50) NOT NULL CHECK (CustomerEmail LIKE '%@gmail.com' OR CustomerEmail LIKE '%@yahoo.co.id'),
    CustomerDOB DATE NOT NULL CHECK(DATEDIFF(YEAR,CustomerDOB,GETDATE()) >17)
)

--Create Table MsStaff
CREATE TABLE MsStaff(
	StaffId CHAR (5) PRIMARY KEY NOT NULL CHECK (StaffId LIKE 'SF[0-9][0-9][0-9]'),
	StaffName VARCHAR (50) NOT NULL CHECK (LEN(StaffName)  > 5),
	StaffGender VARCHAR (7) NOT NULL CHECK (StaffGender IN ('Male','Female')),
	StaffEmail VARCHAR (100) NOT NULL CHECK (StaffEmail LIKE '%@gmail.com' OR StaffEmail LIKE '%@yahoo.co.id'),
	StaffPhoneNumber VARCHAR (50) NOT NULL CHECK (StaffPhoneNumber LIKE '08%'),
	StaffAddress VARCHAR(100) NOT NULL CHECK (StaffAddress LIKE '%Street'),
	StaffDOB DATE NOT NULL CHECK (DATEDIFF(YEAR,StaffDOB,GETDATE()) > 17)
)

--Create Table MsMeatball
CREATE TABLE MsMeatball(
	MeatballId CHAR (5) PRIMARY KEY NOT NULL CHECK (MeatballId LIKE 'MB[0-9][0-9][0-9]'),
	MeatballName VARCHAR (50) NOT NULL,
	MeatballPrice INT NOT NULL CHECK (MeatballPrice BETWEEN 10000 AND 800000)
)

--Create Table MsIngredient
CREATE TABLE MsIngredient(
	IngredientId CHAR (5) PRIMARY KEY NOT NULL CHECK (IngredientId LIKE 'IG[0-9][0-9][0-9]'),
	IngredientName VARCHAR (50) NOT NULL,
	IngredientPrice INT NOT NULL CHECK (IngredientPrice BETWEEN 5000 AND 500000)
)

--Create Table MsRecipe
CREATE TABLE MsRecipe(
	MeatballId CHAR (5) NOT NULL CHECK (MeatballId LIKE 'MB[0-9][0-9][0-9]'),
	IngredientId CHAR (5) NOT NULL CHECK (IngredientId LIKE 'IG[0-9][0-9][0-9]'),
	IngredientQty INT NOT NULL CHECK (IngredientQty > 0),
	PRIMARY KEY(MeatballId,IngredientId),
	CONSTRAINT MeatballId_Recipe_FK FOREIGN KEY (MeatballId) REFERENCES MsMeatball(MeatballId) on delete cascade on update cascade,
	CONSTRAINT IngredientId_Recipe_FK FOREIGN KEY (IngredientId) REFERENCES MsIngredient(IngredientId) on delete cascade on update cascade
)

--Create Table MsHeaderPurchaseTransaction
CREATE TABLE MsHeaderPurchaseTransaction(
	PurchaseTransactionId CHAR (5) PRIMARY KEY NOT NULL CHECK (PurchaseTransactionId LIKE 'PT[0-9][0-9][0-9]'),
	StaffId CHAR (5) NOT NULL CHECK (StaffId LIKE 'SF[0-9][0-9][0-9]'),
	SupplierId CHAR (5) NOT NULL CHECK (SupplierId LIKE 'SP[0-9][0-9][0-9]'),
	PurchaseTransactionDate DATE NOT NULL,
	CONSTRAINT StaffId_PurchaseTransaction_FK FOREIGN KEY (StaffId) REFERENCES MsStaff(StaffId) on delete cascade on update cascade,
	CONSTRAINT SupplierId_PurchaseTransaction_FK FOREIGN KEY (SupplierId) REFERENCES MsSupplier(SupplierId) on delete cascade on update cascade
)

--Create Table MsDetailPurchaseTransaction
CREATE TABLE MsDetailPurchaseTransaction(
	PurchaseTransactionId CHAR (5) NOT NULL CHECK (PurchaseTransactionId LIKE 'PT[0-9][0-9][0-9]'),
	IngredientId CHAR (5) NOT NULL CHECK (IngredientId LIKE 'IG[0-9][0-9][0-9]'),
	PurchaseTransactionQty INT NOT NULL CHECK (PurchaseTransactionQty > 0),
	PRIMARY KEY(PurchaseTransactionId,IngredientId),
	CONSTRAINT PurchaseTransactionId_DetailPurchaseTransaction_FK FOREIGN KEY (PurchaseTransactionId) REFERENCES MsHeaderPurchaseTransaction(PurchaseTransactionId) on delete cascade on update cascade,
	CONSTRAINT IngredientId_DetailPurchaseTransaction_FK FOREIGN KEY (IngredientId) REFERENCES MsIngredient(IngredientId) on delete cascade on update cascade
)

--Create Table MsHeaderSalesTransaction
CREATE TABLE MsHeaderSalesTransaction(
	SalesTransactionId CHAR (5) PRIMARY KEY NOT NULL CHECK (SalesTransactionId LIKE 'ST[0-9][0-9][0-9]'),
	CustomerId CHAR (5) NOT NULL CHECK (CustomerId LIKE 'CT[0-9][0-9][0-9]'),
	StaffId CHAR (5) NOT NULL CHECK (StaffId LIKE 'SF[0-9][0-9][0-9]'),
	SalesTransactionDate DATE NOT NULL,
	CONSTRAINT CustomerId_HeaderSalesTransaction_FK FOREIGN KEY (CustomerId) REFERENCES MsCustomer(CustomerId) on delete cascade on update cascade,
	CONSTRAINT StaffId_HeaderSalesTransaction_FK FOREIGN KEY (StaffId) REFERENCES MsStaff(StaffId) on delete cascade on update cascade
)

--Create Table MsDetailSalesTransaction
CREATE TABLE MsDetailSalesTransaction(
	SalesTransactionId CHAR (5) NOT NULL CHECK (SalesTransactionId LIKE 'ST[0-9][0-9][0-9]'),
	MeatballId CHAR (5) NOT NULL CHECK (MeatballId LIKE 'MB[0-9][0-9][0-9]'),
	SalesTransactionQty INT NOT NULL CHECK (SalesTransactionQty > 0),
	PRIMARY KEY(SalesTransactionId,MeatballId),
	CONSTRAINT SalesTransactionId_DetailSalesTransaction_FK FOREIGN KEY (SalesTransactionId) REFERENCES MsHeaderSalesTransaction(SalesTransactionId) on delete cascade on update cascade,
	CONSTRAINT MeatballId_DetailSalesTransaction_FK FOREIGN KEY (MeatballId) REFERENCES MsMeatball(MeatballId) on delete cascade on update cascade
)