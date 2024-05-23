from datetime import date
from typing import Final, Literal, TypedDict


___all__ = (
    "ALL_DATA_ENTRY_SCHEMA",
    "ALL_DATA_WITH_DATES_ENTRY_SCHEMA",
    "ALL_PREDICTOR_NAMES",
    "PredictorName",
    "PREDICTOR_PORTS_ENTRY_SCHEMA",
    "SignedPredictorsEntry",
    "SIGNED_PREDICTORS_ENTRY_SCHEMA",
)


ALL_PREDICTOR_NAMES: Final = ("AM", "AOP", "AbnormalAccruals", "Accruals", "AccrualsBM", "Activism1", "Activism2", "AdExp", "AgeIPO", "AnalystRevision", "AnalystValue", "AnnouncementReturn", "AssetGrowth", "BM", "BMdec", "BPEBM", "Beta", "BetaFP", "BetaLiquidityPS", "BetaTailRisk", "BidAskSpread", "BookLeverage", "BrandInvest", "CBOperProf", "CF", "CPVolSpread", "Cash", "CashProd", "ChAssetTurnover", "ChEQ", "ChForecastAccrual", "ChInv", "ChInvIA", "ChNAnalyst", "ChNNCOA", "ChNWC", "ChTax", "ChangeInRecommendation", "CitationsRD", "CompEquIss", "CompositeDebtIssuance", "ConsRecomm", "ConvDebt", "CoskewACX", "Coskewness", "CredRatDG", "CustomerMomentum", "DebtIssuance", "DelBreadth", "DelCOA", "DelCOL", "DelDRC", "DelEqu", "DelFINL", "DelLTI", "DelNetFin", "DivInit", "DivOmit", "DivSeason", "DivYieldST", "DolVol", "DownRecomm", "EBM", "EP", "EarnSupBig", "EarningsConsistency", "EarningsForecastDisparity", "EarningsStreak", "EarningsSurprise", "EntMult", "EquityDuration", "ExchSwitch", "ExclExp", "FEPS", "FR", "FirmAge", "FirmAgeMom", "ForecastDispersion", "Frontier", "GP", "Governance", "GrAdExp", "GrLTNOA", "GrSaleToGrInv", "GrSaleToGrOverhead", "Herf", "HerfAsset", "HerfBE", "High52", "IO_ShortInterest", "IdioVol3F", "IdioVolAHT", "Illiquidity", "IndIPO", "IndMom", "IndRetBig", "IntMom", "IntanBM", "IntanCFP", "IntanEP", "IntanSP", "InvGrowth", "InvestPPEInv", "Investment", "LRreversal", "Leverage", "MRreversal", "MS", "MaxRet", "MeanRankRevGrowth", "Mom12m", "Mom12mOffSeason", "Mom6m", "Mom6mJunk", "MomOffSeason", "MomOffSeason06YrPlus", "MomOffSeason11YrPlus", "MomOffSeason16YrPlus", "MomRev", "MomSeason", "MomSeason06YrPlus", "MomSeason11YrPlus", "MomSeason16YrPlus", "MomSeasonShort", "MomVol", "NOA", "NetDebtFinance", "NetDebtPrice", "NetEquityFinance", "NetPayoutYield", "NumEarnIncrease", "OPLeverage", "OScore", "OperProf", "OperProfRD", "OptionVolume1", "OptionVolume2", "OrderBacklog", "OrderBacklogChg", "OrgCap", "PS", "PatentsRD", "PayoutYield", "PctAcc", "PctTotAcc", "PredictedFE", "PriceDelayRsq", "PriceDelaySlope", "PriceDelayTstat", "ProbInformedTrading", "RD", "RDAbility", "RDIPO", "RDS", "RDcap", "REV6", "RIO_Disp", "RIO_MB", "RIO_Turnover", "RIO_Volatility", "RIVolSpread", "RealizedVol", "Recomm_ShortInterest", "ResidualMomentum", "ReturnSkew", "ReturnSkew3F", "RevenueSurprise", "RoE", "SP", "ShareIss1Y", "ShareIss5Y", "ShareRepurchase", "ShareVol", "ShortInterest", "SmileSlope", "Spinoff", "SurpriseRD", "Tax", "TotalAccruals", "TrendFactor", "UpRecomm", "VarCF", "VolMkt", "VolSD", "VolumeTrend", "XFIN", "betaVIX", "cfp", "dCPVolSpread", "dNoa", "dVolCall", "dVolPut", "fgr5yrLag", "grcapx", "grcapx3y", "hire", "iomom_cust", "iomom_supp", "realestate", "retConglomerate", "roaq", "sfe", "sinAlgo", "skew1", "std_turn", "tang", "zerotrade", "zerotradeAlt1", "zerotradeAlt12")
PredictorName = Literal["AM", "AOP", "AbnormalAccruals", "Accruals", "AccrualsBM", "Activism1", "Activism2", "AdExp", "AgeIPO", "AnalystRevision", "AnalystValue", "AnnouncementReturn", "AssetGrowth", "BM", "BMdec", "BPEBM", "Beta", "BetaFP", "BetaLiquidityPS", "BetaTailRisk", "BidAskSpread", "BookLeverage", "BrandInvest", "CBOperProf", "CF", "CPVolSpread", "Cash", "CashProd", "ChAssetTurnover", "ChEQ", "ChForecastAccrual", "ChInv", "ChInvIA", "ChNAnalyst", "ChNNCOA", "ChNWC", "ChTax", "ChangeInRecommendation", "CitationsRD", "CompEquIss", "CompositeDebtIssuance", "ConsRecomm", "ConvDebt", "CoskewACX", "Coskewness", "CredRatDG", "CustomerMomentum", "DebtIssuance", "DelBreadth", "DelCOA", "DelCOL", "DelDRC", "DelEqu", "DelFINL", "DelLTI", "DelNetFin", "DivInit", "DivOmit", "DivSeason", "DivYieldST", "DolVol", "DownRecomm", "EBM", "EP", "EarnSupBig", "EarningsConsistency", "EarningsForecastDisparity", "EarningsStreak", "EarningsSurprise", "EntMult", "EquityDuration", "ExchSwitch", "ExclExp", "FEPS", "FR", "FirmAge", "FirmAgeMom", "ForecastDispersion", "Frontier", "GP", "Governance", "GrAdExp", "GrLTNOA", "GrSaleToGrInv", "GrSaleToGrOverhead", "Herf", "HerfAsset", "HerfBE", "High52", "IO_ShortInterest", "IdioVol3F", "IdioVolAHT", "Illiquidity", "IndIPO", "IndMom", "IndRetBig", "IntMom", "IntanBM", "IntanCFP", "IntanEP", "IntanSP", "InvGrowth", "InvestPPEInv", "Investment", "LRreversal", "Leverage", "MRreversal", "MS", "MaxRet", "MeanRankRevGrowth", "Mom12m", "Mom12mOffSeason", "Mom6m", "Mom6mJunk", "MomOffSeason", "MomOffSeason06YrPlus", "MomOffSeason11YrPlus", "MomOffSeason16YrPlus", "MomRev", "MomSeason", "MomSeason06YrPlus", "MomSeason11YrPlus", "MomSeason16YrPlus", "MomSeasonShort", "MomVol", "NOA", "NetDebtFinance", "NetDebtPrice", "NetEquityFinance", "NetPayoutYield", "NumEarnIncrease", "OPLeverage", "OScore", "OperProf", "OperProfRD", "OptionVolume1", "OptionVolume2", "OrderBacklog", "OrderBacklogChg", "OrgCap", "PS", "PatentsRD", "PayoutYield", "PctAcc", "PctTotAcc", "PredictedFE", "PriceDelayRsq", "PriceDelaySlope", "PriceDelayTstat", "ProbInformedTrading", "RD", "RDAbility", "RDIPO", "RDS", "RDcap", "REV6", "RIO_Disp", "RIO_MB", "RIO_Turnover", "RIO_Volatility", "RIVolSpread", "RealizedVol", "Recomm_ShortInterest", "ResidualMomentum", "ReturnSkew", "ReturnSkew3F", "RevenueSurprise", "RoE", "SP", "ShareIss1Y", "ShareIss5Y", "ShareRepurchase", "ShareVol", "ShortInterest", "SmileSlope", "Spinoff", "SurpriseRD", "Tax", "TotalAccruals", "TrendFactor", "UpRecomm", "VarCF", "VolMkt", "VolSD", "VolumeTrend", "XFIN", "betaVIX", "cfp", "dCPVolSpread", "dNoa", "dVolCall", "dVolPut", "fgr5yrLag", "grcapx", "grcapx3y", "hire", "iomom_cust", "iomom_supp", "realestate", "retConglomerate", "roaq", "sfe", "sinAlgo", "skew1", "std_turn", "tang", "zerotrade", "zerotradeAlt1", "zerotradeAlt12"]


class SignedPredictorsEntry(TypedDict):
    """This type is simply a `dict` with type hinting."""
    permno: int
    yyyymm: str
    AM: float | None
    AOP: float | None
    AbnormalAccruals: float | None
    Accruals: float | None
    AccrualsBM: float | None
    Activism1: float | None
    Activism2: float | None
    AdExp: float | None
    AgeIPO: float | None
    AnalystRevision: float | None
    AnalystValue: float | None
    AnnouncementReturn: float | None
    AssetGrowth: float | None
    BM: float | None
    BMdec: float | None
    BPEBM: float | None
    Beta: float | None
    BetaFP: float | None
    BetaLiquidityPS: float | None
    BetaTailRisk: float | None
    BidAskSpread: float | None
    BookLeverage: float | None
    BrandInvest: float | None
    CBOperProf: float | None
    CF: float | None
    CPVolSpread: float | None
    Cash: float | None
    CashProd: float | None
    ChAssetTurnover: float | None
    ChEQ: float | None
    ChForecastAccrual: float | None
    ChInv: float | None
    ChInvIA: float | None
    ChNAnalyst: float | None
    ChNNCOA: float | None
    ChNWC: float | None
    ChTax: float | None
    ChangeInRecommendation: float | None
    CitationsRD: float | None
    CompEquIss: float | None
    CompositeDebtIssuance: float | None
    ConsRecomm: float | None
    ConvDebt: float | None
    CoskewACX: float | None
    Coskewness: float | None
    CredRatDG: float | None
    CustomerMomentum: float | None
    DebtIssuance: float | None
    DelBreadth: float | None
    DelCOA: float | None
    DelCOL: float | None
    DelDRC: float | None
    DelEqu: float | None
    DelFINL: float | None
    DelLTI: float | None
    DelNetFin: float | None
    DivInit: float | None
    DivOmit: float | None
    DivSeason: float | None
    DivYieldST: float | None
    DolVol: float | None
    DownRecomm: float | None
    EBM: float | None
    EP: float | None
    EarnSupBig: float | None
    EarningsConsistency: float | None
    EarningsForecastDisparity: float | None
    EarningsStreak: float | None
    EarningsSurprise: float | None
    EntMult: float | None
    EquityDuration: float | None
    ExchSwitch: float | None
    ExclExp: float | None
    FEPS: float | None
    FR: float | None
    FirmAge: float | None
    FirmAgeMom: float | None
    ForecastDispersion: float | None
    Frontier: float | None
    GP: float | None
    Governance: float | None
    GrAdExp: float | None
    GrLTNOA: float | None
    GrSaleToGrInv: float | None
    GrSaleToGrOverhead: float | None
    Herf: float | None
    HerfAsset: float | None
    HerfBE: float | None
    High52: float | None
    IO_ShortInterest: float | None
    IdioVol3F: float | None
    IdioVolAHT: float | None
    Illiquidity: float | None
    IndIPO: float | None
    IndMom: float | None
    IndRetBig: float | None
    IntMom: float | None
    IntanBM: float | None
    IntanCFP: float | None
    IntanEP: float | None
    IntanSP: float | None
    InvGrowth: float | None
    InvestPPEInv: float | None
    Investment: float | None
    LRreversal: float | None
    Leverage: float | None
    MRreversal: float | None
    MS: float | None
    MaxRet: float | None
    MeanRankRevGrowth: float | None
    Mom12m: float | None
    Mom12mOffSeason: float | None
    Mom6m: float | None
    Mom6mJunk: float | None
    MomOffSeason: float | None
    MomOffSeason06YrPlus: float | None
    MomOffSeason11YrPlus: float | None
    MomOffSeason16YrPlus: float | None
    MomRev: float | None
    MomSeason: float | None
    MomSeason06YrPlus: float | None
    MomSeason11YrPlus: float | None
    MomSeason16YrPlus: float | None
    MomSeasonShort: float | None
    MomVol: float | None
    NOA: float | None
    NetDebtFinance: float | None
    NetDebtPrice: float | None
    NetEquityFinance: float | None
    NetPayoutYield: float | None
    NumEarnIncrease: float | None
    OPLeverage: float | None
    OScore: float | None
    OperProf: float | None
    OperProfRD: float | None
    OptionVolume1: float | None
    OptionVolume2: float | None
    OrderBacklog: float | None
    OrderBacklogChg: float | None
    OrgCap: float | None
    PS: float | None
    PatentsRD: float | None
    PayoutYield: float | None
    PctAcc: float | None
    PctTotAcc: float | None
    PredictedFE: float | None
    PriceDelayRsq: float | None
    PriceDelaySlope: float | None
    PriceDelayTstat: float | None
    ProbInformedTrading: float | None
    RD: float | None
    RDAbility: float | None
    RDIPO: float | None
    RDS: float | None
    RDcap: float | None
    REV6: float | None
    RIO_Disp: float | None
    RIO_MB: float | None
    RIO_Turnover: float | None
    RIO_Volatility: float | None
    RIVolSpread: float | None
    RealizedVol: float | None
    Recomm_ShortInterest: float | None
    ResidualMomentum: float | None
    ReturnSkew: float | None
    ReturnSkew3F: float | None
    RevenueSurprise: float | None
    RoE: float | None
    SP: float | None
    ShareIss1Y: float | None
    ShareIss5Y: float | None
    ShareRepurchase: float | None
    ShareVol: float | None
    ShortInterest: float | None
    SmileSlope: float | None
    Spinoff: float | None
    SurpriseRD: float | None
    Tax: float | None
    TotalAccruals: float | None
    TrendFactor: float | None
    UpRecomm: float | None
    VarCF: float | None
    VolMkt: float | None
    VolSD: float | None
    VolumeTrend: float | None
    XFIN: float | None
    betaVIX: float | None
    cfp: float | None
    dCPVolSpread: float | None
    dNoa: float | None
    dVolCall: float | None
    dVolPut: float | None
    fgr5yrLag: float | None
    grcapx: float | None
    grcapx3y: float | None
    hire: float | None
    iomom_cust: float | None
    iomom_supp: float | None
    realestate: float | None
    retConglomerate: float | None
    roaq: float | None
    sfe: float | None
    sinAlgo: float | None
    skew1: float | None
    std_turn: float | None
    tang: float | None
    zerotrade: float | None
    zerotradeAlt1: float | None
    zerotradeAlt12: float | None


SIGNED_PREDICTORS_ENTRY_SCHEMA: Final = {
    "permno": int,
    "yyyymm": str,
    "AM": float,
    "AOP": float,
    "AbnormalAccruals": float,
    "Accruals": float,
    "AccrualsBM": float,
    "Activism1": float,
    "Activism2": float,
    "AdExp": float,
    "AgeIPO": float,
    "AnalystRevision": float,
    "AnalystValue": float,
    "AnnouncementReturn": float,
    "AssetGrowth": float,
    "BM": float,
    "BMdec": float,
    "BPEBM": float,
    "Beta": float,
    "BetaFP": float,
    "BetaLiquidityPS": float,
    "BetaTailRisk": float,
    "BidAskSpread": float,
    "BookLeverage": float,
    "BrandInvest": float,
    "CBOperProf": float,
    "CF": float,
    "CPVolSpread": float,
    "Cash": float,
    "CashProd": float,
    "ChAssetTurnover": float,
    "ChEQ": float,
    "ChForecastAccrual": float,
    "ChInv": float,
    "ChInvIA": float,
    "ChNAnalyst": float,
    "ChNNCOA": float,
    "ChNWC": float,
    "ChTax": float,
    "ChangeInRecommendation": float,
    "CitationsRD": float,
    "CompEquIss": float,
    "CompositeDebtIssuance": float,
    "ConsRecomm": float,
    "ConvDebt": float,
    "CoskewACX": float,
    "Coskewness": float,
    "CredRatDG": float,
    "CustomerMomentum": float,
    "DebtIssuance": float,
    "DelBreadth": float,
    "DelCOA": float,
    "DelCOL": float,
    "DelDRC": float,
    "DelEqu": float,
    "DelFINL": float,
    "DelLTI": float,
    "DelNetFin": float,
    "DivInit": float,
    "DivOmit": float,
    "DivSeason": float,
    "DivYieldST": float,
    "DolVol": float,
    "DownRecomm": float,
    "EBM": float,
    "EP": float,
    "EarnSupBig": float,
    "EarningsConsistency": float,
    "EarningsForecastDisparity": float,
    "EarningsStreak": float,
    "EarningsSurprise": float,
    "EntMult": float,
    "EquityDuration": float,
    "ExchSwitch": float,
    "ExclExp": float,
    "FEPS": float,
    "FR": float,
    "FirmAge": float,
    "FirmAgeMom": float,
    "ForecastDispersion": float,
    "Frontier": float,
    "GP": float,
    "Governance": float,
    "GrAdExp": float,
    "GrLTNOA": float,
    "GrSaleToGrInv": float,
    "GrSaleToGrOverhead": float,
    "Herf": float,
    "HerfAsset": float,
    "HerfBE": float,
    "High52": float,
    "IO_ShortInterest": float,
    "IdioVol3F": float,
    "IdioVolAHT": float,
    "Illiquidity": float,
    "IndIPO": float,
    "IndMom": float,
    "IndRetBig": float,
    "IntMom": float,
    "IntanBM": float,
    "IntanCFP": float,
    "IntanEP": float,
    "IntanSP": float,
    "InvGrowth": float,
    "InvestPPEInv": float,
    "Investment": float,
    "LRreversal": float,
    "Leverage": float,
    "MRreversal": float,
    "MS": float,
    "MaxRet": float,
    "MeanRankRevGrowth": float,
    "Mom12m": float,
    "Mom12mOffSeason": float,
    "Mom6m": float,
    "Mom6mJunk": float,
    "MomOffSeason": float,
    "MomOffSeason06YrPlus": float,
    "MomOffSeason11YrPlus": float,
    "MomOffSeason16YrPlus": float,
    "MomRev": float,
    "MomSeason": float,
    "MomSeason06YrPlus": float,
    "MomSeason11YrPlus": float,
    "MomSeason16YrPlus": float,
    "MomSeasonShort": float,
    "MomVol": float,
    "NOA": float,
    "NetDebtFinance": float,
    "NetDebtPrice": float,
    "NetEquityFinance": float,
    "NetPayoutYield": float,
    "NumEarnIncrease": float,
    "OPLeverage": float,
    "OScore": float,
    "OperProf": float,
    "OperProfRD": float,
    "OptionVolume1": float,
    "OptionVolume2": float,
    "OrderBacklog": float,
    "OrderBacklogChg": float,
    "OrgCap": float,
    "PS": float,
    "PatentsRD": float,
    "PayoutYield": float,
    "PctAcc": float,
    "PctTotAcc": float,
    "PredictedFE": float,
    "PriceDelayRsq": float,
    "PriceDelaySlope": float,
    "PriceDelayTstat": float,
    "ProbInformedTrading": float,
    "RD": float,
    "RDAbility": float,
    "RDIPO": float,
    "RDS": float,
    "RDcap": float,
    "REV6": float,
    "RIO_Disp": float,
    "RIO_MB": float,
    "RIO_Turnover": float,
    "RIO_Volatility": float,
    "RIVolSpread": float,
    "RealizedVol": float,
    "Recomm_ShortInterest": float,
    "ResidualMomentum": float,
    "ReturnSkew": float,
    "ReturnSkew3F": float,
    "RevenueSurprise": float,
    "RoE": float,
    "SP": float,
    "ShareIss1Y": float,
    "ShareIss5Y": float,
    "ShareRepurchase": float,
    "ShareVol": float,
    "ShortInterest": float,
    "SmileSlope": float,
    "Spinoff": float,
    "SurpriseRD": float,
    "Tax": float,
    "TotalAccruals": float,
    "TrendFactor": float,
    "UpRecomm": float,
    "VarCF": float,
    "VolMkt": float,
    "VolSD": float,
    "VolumeTrend": float,
    "XFIN": float,
    "betaVIX": float,
    "cfp": float,
    "dCPVolSpread": float,
    "dNoa": float,
    "dVolCall": float,
    "dVolPut": float,
    "fgr5yrLag": float,
    "grcapx": float,
    "grcapx3y": float,
    "hire": float,
    "iomom_cust": float,
    "iomom_supp": float,
    "realestate": float,
    "retConglomerate": float,
    "roaq": float,
    "sfe": float,
    "sinAlgo": float,
    "skew1": float,
    "std_turn": float,
    "tang": float,
    "zerotrade": float,
    "zerotradeAlt1": float,
    "zerotradeAlt12": float,
}


ALL_DATA_ENTRY_SCHEMA: Final = SIGNED_PREDICTORS_ENTRY_SCHEMA | {
    "STreversal": float,
    "Price": float,
    "Size": float,
}


ALL_DATA_WITH_DATES_ENTRY_SCHEMA: Final = ALL_DATA_ENTRY_SCHEMA | {
    "date": date,
    "date_right": date,
}
