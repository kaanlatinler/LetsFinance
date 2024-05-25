create table DovizData(
	DovizDataID int primary key identity,
	DovizID uniqueidentifier not null,
	DovizName nvarchar(100),
	DovizSellPrice nvarchar(100),
	DovizBuyPrice nvarchar(100),
	DovizCode nvarchar(10)
)