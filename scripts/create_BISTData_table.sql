create table BISTData(
	BISTDataID int primary key identity,
	BISTID uniqueidentifier not null,
	BISTName nvarchar(100),
	BISTSellPrice nvarchar(10)
)