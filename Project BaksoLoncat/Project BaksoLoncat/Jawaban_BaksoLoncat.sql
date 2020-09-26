USE BaksoLoncat
GO
--Jawaban dari Soal

--1
SELECT 
	CustomerName,
	[SalesTransactionID] = 'Sales ID ' + RIGHT(HST.SalesTransactionId,3),
	[Total item Bought] = SUM(SalesTransactionQty)
FROM MsCustomer MC
JOIN MsHeaderSalesTransaction HST
ON MC.CustomerId = HST.CustomerId
JOIN MsDetailSalesTransaction DST
ON HST.SalesTransactionId = DST.SalesTransactionId
WHERE CustomerGender LIKE 'Female'  AND 
	DATEPART(YEAR,HST.SalesTransactionDate) > 2015
GROUP BY CustomerName,HST.SalesTransactionId

--2
SELECT
	StaffGender,
	[Customer Count] = COUNT(MC.CustomerId)
FROM MsStaff MS
JOIN MsHeaderSalesTransaction HST
ON MS.StaffId = HST.StaffId
JOIN MsCustomer MC
ON MC.CustomerId = HST.CustomerId
WHERE 
	DATEPART(MONTH,HST.SalesTransactionDate) < 6 AND
	DATEDIFF(YEAR,StaffDOB,GETDATE()) < 30
GROUP BY StaffGender

--3
SELECT MS.SupplierId,
	[Ingredient Count] = SUM(PurchaseTransactionQty),
	[Total Transaction Price] = 'Rp.' + CAST(SUM(PurchaseTransactionQty) * IngredientPrice as VARCHAR (50))
FROM MsSupplier MS
JOIN MsHeaderPurchaseTransaction HPT
ON MS.SupplierId = HPT.SupplierId
JOIN MsDetailPurchaseTransaction DPT
ON HPT.PurchaseTransactionId = DPT.PurchaseTransactionId
JOIN MsIngredient MI
ON MI.IngredientId = DPT.IngredientId
WHERE DATEPART(MONTH,HPT.PurchaseTransactionDate) > 6 AND
	PurchaseTransactionQty > 2
GROUP BY MS.SupplierId,IngredientPrice

--4
SELECT StaffGender,
	[Average Age] = AVG(DATEDIFF(YEAR,StaffDOB,GETDATE())),
	[Supplier Count] = COUNT(MSP.SupplierId)
FROM MsStaff MS
JOIN MsHeaderPurchaseTransaction HPT
ON MS.StaffId = HPT.StaffId
JOIN MsSupplier MSP
ON MSP.SupplierId = HPT.SupplierId
WHERE DATEDIFF(DAY,PurchaseTransactionDate,GETDATE()) >= 15 AND
	DATENAME(MONTH,StaffDOB) IN ('January','February','April','May','November','December')
GROUP BY StaffGender


--5
SELECT DISTINCT SupplierName,
	[SupplierPhone] = STUFF(MS.SupplierPhoneNumber,1,2,'+62')
FROM 
(
	SELECT MAX(IngredientPrice / 2) AS 'HALF' FROM MsIngredient
) AS HALFPRICE,
MsSupplier MS
JOIN MsHeaderPurchaseTransaction HPT
ON MS.SupplierId = HPT.SupplierId
JOIN MsDetailPurchaseTransaction DPT
ON HPT.PurchaseTransactionId = DPT.PurchaseTransactionId
JOIN MsIngredient MI
ON MI.IngredientId = DPT.IngredientId
WHERE IngredientPrice <= HALFPRICE.HALF AND
	SupplierEmail LIKE '%@gmail.com'
GROUP BY SupplierPhoneNumber,SupplierName
ORDER BY SupplierName DESC

--6
SELECT DISTINCT CustomerName,
	[Customer Username] =  Supplier.Username
FROM (
	SELECT AVG(MeatballPrice) AS AVERAGEPrice FROM MsMeatball
)AS Meatball,(
	SELECT SUBSTRING(SupplierEmail,1,CHARINDEX('@',SupplierEmail)-1) AS Username FROM MsSupplier
)AS Supplier,MsCustomer MC
JOIN MsHeaderSalesTransaction HST
ON HST.CustomerId = MC.CustomerId
JOIN MsDetailSalesTransaction DST
ON DST.SalesTransactionId = HST.SalesTransactionId
JOIN MsMeatball MM
ON MM.MeatballId = DST.MeatballId
WHERE MeatballPrice > Meatball.AVERAGEPrice AND
	CustomerName LIKE '% %'

--7
SELECT MS.SupplierId,
	CASE WHEN CHARINDEX(' ',SupplierName) = 0
	THEN SupplierName
	ELSE SUBSTRING(SupplierName,1,CHARINDEX(' ',SupplierName))
	END AS [First Name]
FROM (
	SELECT ((4/3) * MIN(IngredientPrice)) AS BOTTOM FROM MsIngredient
)AS MINIMUM,
(
	SELECT AVG(IngredientPrice) AS AVERAGEPrice FROM MsIngredient
)AS Maximum,MsSupplier MS
JOIN MsHeaderPurchaseTransaction HPT
ON HPT.SupplierId = MS.SupplierId
JOIN MsDetailPurchaseTransaction DPT
ON DPT.PurchaseTransactionId = HPT.PurchaseTransactionId
JOIN MsIngredient MI
ON MI.IngredientId = DPT.IngredientId
WHERE IngredientPrice BETWEEN MINIMUM.BOTTOM AND Maximum.AVERAGEPrice AND
	DATEPART(MONTH,HPT.PurchaseTransactionDate) > 5

--8
SELECT DISTINCT MC.CustomerId,
	CustomerName,
	[Transaction Month] = DATENAME(MONTH,SalesTransactionDate)
FROM(
	SELECT AVG(MeatballPrice) AS AVERAGEPrice FROM MsMeatball
)AS MeatballMin,
(
	SELECT MAX(MeatballPrice) AS MAXPrice FROM MsMeatball
)AS MeatballMax,
MsCustomer MC
JOIN MsHeaderSalesTransaction HST
ON MC.CustomerId = HST.CustomerId 
JOIN MsDetailSalesTransaction DST
ON DST.SalesTransactionId = HST.SalesTransactionId
JOIN MsMeatball MM
ON MM.MeatballId = DST.MeatballId
WHERE MeatballPrice < MeatballMin.AVERAGEPrice OR
	MeatballPrice = MeatballMax.MAXPrice AND
	DATEDIFF(MONTH,SalesTransactionDate,GETDATE()) > 1
	
--9
CREATE VIEW [ViewMeatBallStats] AS
SELECT MM.MeatballId,
	[MeatBallCode] = UPPER(SUBSTRING(MeatballName,1,3)) + CAST(SUBSTRING(MM.MeatballId,3,5) AS VARCHAR (5)),
	[MeatBall Count] = SUM(SalesTransactionQty),
	[Total MeatBall Price] = SUM(SalesTransactionQty) * MeatballPrice
FROM MsMeatball MM
JOIN MsDetailSalesTransaction DST
ON DST.MeatballId = MM.MeatballId
JOIN MsRecipe MR
ON MR.MeatballId = MM.MeatballId
WHERE MeatballPrice < 50000 AND
	IngredientQty > 50
GROUP BY MM.MeatballId,MeatballName,MeatballPrice

SELECT * FROM [ViewMeatBallStats] --Setelah menggunakan WHERE tidak ada data yang memenuhi kondisi

--10
CREATE VIEW [ViewIngredientSpending] AS
SELECT
	MI.IngredientId,
	[Total Item] = COUNT(DST.SalesTransactionId),
	[Total Spending] = CAST(SUM(SalesTransactionQty) - (IngredientQty * (IngredientPrice / 1000)) AS VARCHAR(100)) + 'K'
FROM MsIngredient MI
JOIN MsRecipe MR
ON MR.IngredientId = MI.IngredientId
JOIN MsMeatball MM
ON MM.MeatballId = MR.MeatballId
JOIN MsDetailSalesTransaction DST
ON DST.MeatballId = MM.MeatballId
JOIN MsHeaderSalesTransaction HST
ON HST.SalesTransactionId = DST.SalesTransactionId
WHERE SalesTransactionQty < 200 AND
	  DATEPART(DAY,SalesTransactionDate) >= 15
GROUP BY MI.IngredientId,IngredientQty,IngredientPrice

GO

SELECT * FROM [ViewIngredientSpending]