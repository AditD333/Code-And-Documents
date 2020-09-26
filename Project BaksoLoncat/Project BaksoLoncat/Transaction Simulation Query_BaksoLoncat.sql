USE BaksoLoncat
GO

--Insert Header Purchase Transaction
CREATE PROC [Insert_Header_Purchase_Transaction]
@PurchaseTransactionId CHAR (5),
@StaffId CHAR (5),
@SupplierId CHAR (5),
@TransactionDate VARCHAR (50)
AS
BEGIN
	IF(LEN(@PurchaseTransactionId) > 0)
	BEGIN
		IF(NOT EXISTS(SELECT * FROM MsHeaderPurchaseTransaction WHERE PurchaseTransactionId LIKE @PurchaseTransactionId))
		BEGIN
			IF(LEN(@StaffId) > 0)
			BEGIN
				IF(EXISTS(SELECT * FROM MsStaff WHERE StaffId LIKE @StaffId))
				BEGIN
					IF(LEN(@SupplierId) > 0)
					BEGIN
						IF(EXISTS(SELECT * FROM MsSupplier WHERE SupplierId LIKE @SupplierId))
						BEGIN
							IF(LEN(@TransactionDate) > 0)
							BEGIN
								IF(ISDATE(@TransactionDate) = 1)
								BEGIN
									INSERT INTO MsHeaderPurchaseTransaction
										(PurchaseTransactionId,StaffId,SupplierId,PurchaseTransactionDate)
									VALUES
										(@PurchaseTransactionId,@StaffId,@SupplierId,@TransactionDate)
									PRINT 'Successfullly Insert Header Purchase Transaction Data';
								END
								ELSE
								BEGIN
									PRINT  'Error... Date Format wrong [YYYY-MM-DD]';
								END
							END
							ELSE
							BEGIN
								PRINT 'Error... Transaction Date is empty';
							END
						END
						ELSE
						BEGIN
							PRINT 'Error... Supplier Not Found';
						END
					END
					ELSE
					BEGIN
						PRINT 'Error... Supplier Id is empty';
					END
				END
				ELSE
				BEGIN
					PRINT 'Error... Staff Not Found';
				END
			END
			ELSE
			BEGIN
				PRINT 'Error... Staff Id is empty ';
			END
		END
		ELSE
		BEGIN
			PRINT 'Error... Purchase Id Duplicate';
		END
	END
	ELSE
	BEGIN
		PRINT 'Error... Purchase Id is empty';
	END
END

Insert_Header_Purchase_Transaction'PT016','SF001','SP001','2020-01-20'

SELECT * FROM MsHeaderPurchaseTransaction

--Insert Detail Purchase Transaction
CREATE PROC [Insert_Detail_Purchase_Transaction]
@PurchaseTransactionId CHAR (5),
@IngredienId CHAR (5),
@Quantity VARCHAR (10)
AS
BEGIN
	IF(LEN(@PurchaseTransactionId) > 0)
	BEGIN
		IF(EXISTS(SELECT * FROM MsHeaderPurchaseTransaction WHERE PurchaseTransactionId LIKE @PurchaseTransactionId))
		BEGIN
			IF(LEN(@IngredienId) > 0)
			BEGIN
				IF(EXISTS(SELECT * FROM MsIngredient WHERE IngredientId LIKE @IngredienId))
				BEGIN
					IF(LEN(@Quantity) > 0)
					BEGIN
						IF(CAST(@Quantity AS INT) > 0)
						BEGIN
							INSERT INTO MsDetailPurchaseTransaction
							(PurchaseTransactionId,IngredientId,PurchaseTransactionQty)
						VALUES
							(@PurchaseTransactionId,@IngredienId,@Quantity)
							PRINT 'Successfully Insert Detail Transaction Data'
						END
						ELSE
						BEGIN
							PRINT 'Error... Quantity must be more than 0';
						END
					END
					ELSE
					BEGIN
						PRINT 'Error... Quantity is empty';
					END
				END
				ELSE
				BEGIN
					PRINT 'Error... Ingdiend Not Found';
				END
			END
			ELSE
			BEGIN
				PRINT 'Error... Ingridient Id is empty';
			END
		END
		ELSE
		BEGIN
			PRINT 'Error... Purchase Id not found';
		END
	END
	ELSE
	BEGIN
		PRINT 'Error... Purchase Id is empty';
	END
END

Insert_Detail_Purchase_Transaction'PT016','IG001','2'

SELECT * FROM MsDetailPurchaseTransaction

--Insert Header Sales Transaction
CREATE PROC [Insert_Header_Sales_Transaction]
@SalesTransactionId CHAR (5),
@CustomerId CHAR (5),
@StaffId CHAR (5),
@TransactionDate VARCHAR (50)
AS
BEGIN
	IF(LEN(@SalesTransactionId) > 0)
	BEGIN
		IF(NOT EXISTS(SELECT * FROM MsHeaderSalesTransaction WHERE SalesTransactionId LIKE @SalesTransactionId))
		BEGIN
			IF(LEN(@CustomerId) > 0)
			BEGIN
				IF(EXISTS(SELECT * FROM MsCustomer WHERE CustomerId LIKE @CustomerId))
				BEGIN
					IF(LEN(@StaffId) > 0)
					BEGIN
						IF(EXISTS(SELECT * FROM MsStaff WHERE StaffId LIKE @StaffId))
						BEGIN
							IF(LEN(@TransactionDate) > 0)
							BEGIN
								IF(ISDATE(@TransactionDate) = 1)
								BEGIN
									INSERT INTO MsHeaderSalesTransaction
										(SalesTransactionId,CustomerId,StaffId,SalesTransactionDate)
									VALUES
										(@SalesTransactionId,@CustomerId,@StaffId,@TransactionDate)
									PRINT 'Successfullly Insert Header Sales Transaction Data';
								END
								ELSE
								BEGIN
									PRINT  'Error... Date Format wrong [YYYY-MM-DD]';
								END
							END
							ELSE
							BEGIN
								PRINT 'Error... Transaction Date is empty';
							END
						END
						ELSE
						BEGIN
							PRINT 'Error... Staff Not Found';
						END
					END
					ELSE
					BEGIN
						PRINT 'Error... Staff Id is empty ';
					END
				END
				ELSE
				BEGIN
					PRINT 'Error... Customer Not Found';
				END

			END
			ELSE
			BEGIN
				PRINT 'Error... Customer Id is empty';
			END
		END
		ELSE
		BEGIN
			PRINT 'Error... Sales Id Duplicate';
		END
	END
	ELSE
	BEGIN
		PRINT 'Error... Sales Id is empty';
	END
END

Insert_Header_Sales_Transaction'ST016','CT010','SF001','2020-01-20'

SELECT * FROM MsHeaderSalesTransaction

--Insert Detail Sales Transaction
CREATE PROC [Insert_Detail_Sales_Transaction]
@SalesTransactionId CHAR (5),
@MeatballId CHAR (5),
@Quantity VARCHAR (10)
AS
BEGIN
	IF(LEN(@SalesTransactionId) > 0)
	BEGIN
		IF(EXISTS(SELECT * FROM MsHeaderSalesTransaction WHERE SalesTransactionId LIKE @SalesTransactionId))
		BEGIN
			IF(LEN(@MeatballId) > 0)
			BEGIN
				IF(EXISTS(SELECT * FROM MsMeatball WHERE MeatballId LIKE @MeatballId))
				BEGIN
					IF(LEN(@Quantity) > 0)
					BEGIN
						IF(CAST(@Quantity AS INT) > 0)
						BEGIN
							INSERT INTO MsDetailSalesTransaction
								(SalesTransactionId,MeatballId,SalesTransactionQty)
							VALUES
								(@SalesTransactionId,@MeatballId,@Quantity)
							PRINT 'Successfully Insert Detail Transaction Data'
						END
						ELSE
						BEGIN
							PRINT 'Error... Quantity must be more than 0';
						END
					END
					ELSE
					BEGIN
						PRINT 'Error... Quantity is empty';
					END
				END
				ELSE
				BEGIN
					PRINT 'Error... Meatball Not Found';
				END
			END
			ELSE
			BEGIN
				PRINT 'Error... Meatball Id is empty';
			END
		END
		ELSE
		BEGIN
			PRINT 'Error... Sales Id not found';
		END
	END
	ELSE
	BEGIN
		PRINT 'Error... Sales Id is empty';
	END
END

Insert_Detail_Sales_Transaction'ST016','MB003','3'

SELECT * FROM MsDetailSalesTransaction