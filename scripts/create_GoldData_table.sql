create table GoldData(
	GoldDataID int primary key identity,
	GoldID uniqueidentifier not null,
	GoldName nvarchar(100),
	GoldSellPrice nvarchar(10)
)