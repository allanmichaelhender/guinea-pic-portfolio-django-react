from .models import FtseData, Snp500Data, Nikkei225Data, EuronextData, SseData


def invest_daily(
    amount_daily,
    start_date,
    end_date,
    FTSE_weight=0,
    SNP500_weight=0,
    NIKKEI225_weight=0,
    EURONEXT_weight=0,
    SSE_weight=0,
    FTSE_queryset=None,
    SNP500_queryset=None,
    NIKKEI225_queryset=None,
    EURONEXT_queryset=None,
    SSE_queryset=None,
):
    FTSE_total_shares = 0
    SNP500_total_shares = 0
    NIKKEI225_total_shares = 0
    EURONEXT_total_shares = 0
    SSE_total_shares = 0

    FTSE_value = 0
    SNP500_value = 0
    NIKKEI225_value = 0
    EURONEXT_value = 0
    SSE_value = 0

    timeframe = end_date - start_date
    total_days = timeframe.days
    total_amount_to_invest = total_days * amount_daily

    if FTSE_queryset is not None and len(FTSE_queryset) != 0:
        FTSE_aggregated_amount_per_day = total_amount_to_invest / (
            len(FTSE_queryset) + 1
        )

        for daily_entry in FTSE_queryset.iterator():
            print(daily_entry)
            FTSE_total_shares += (
                float(FTSE_aggregated_amount_per_day) / float(daily_entry.close)
            ) * float(FTSE_weight)
            FTSE_value = FTSE_total_shares * float(daily_entry.close)

    if SNP500_queryset is not None and len(SNP500_queryset) != 0:
        SNP500_aggregated_amount_per_day = total_amount_to_invest / (
            len(SNP500_queryset) + 1
        )

        for daily_entry in SNP500_queryset:
            SNP500_total_shares += (
                float(SNP500_aggregated_amount_per_day) / float(daily_entry.close)
            ) * float(SNP500_weight)
            SNP500_value = SNP500_total_shares * float(daily_entry.close)

    if NIKKEI225_queryset is not None and len(NIKKEI225_queryset) != 0:
        NIKKEI225_aggregated_amount_per_day = total_amount_to_invest / (
            len(NIKKEI225_queryset) + 1
        )

        for daily_entry in NIKKEI225_queryset:
            NIKKEI225_total_shares += (
                float(NIKKEI225_aggregated_amount_per_day) / float(daily_entry.close)
            ) * float(NIKKEI225_weight)
            NIKKEI225_value = NIKKEI225_total_shares * float(daily_entry.close)

    if EURONEXT_queryset is not None and len(EURONEXT_queryset) != 0:
        EURONEXT_aggregated_amount_per_day = total_amount_to_invest / (
            len(EURONEXT_queryset) + 1
        )

        for daily_entry in EURONEXT_queryset:
            EURONEXT_total_shares += (
                float(EURONEXT_aggregated_amount_per_day) / float(daily_entry.close)
            ) * float(EURONEXT_weight)
            EURONEXT_value = EURONEXT_total_shares * float(daily_entry.close)

    if SSE_queryset is not None and len(SSE_queryset) != 0:
        SSE_aggregated_amount_per_day = total_amount_to_invest / (len(SSE_queryset) + 1)

        for daily_entry in SSE_queryset:
            SSE_total_shares += (
                float(SSE_aggregated_amount_per_day) / float(daily_entry.close)
            ) * float(SSE_weight)
            SSE_value = SSE_total_shares * float(daily_entry.close)

    return {
        "total_invested": total_amount_to_invest,
        "end_value": FTSE_value
        + SNP500_value
        + NIKKEI225_value
        + EURONEXT_value
        + SSE_value,
    }


def invest_monthly(
    amount_monthly,
    start_date,
    end_date,
    FTSE_weight=0,
    SNP500_weight=0,
    NIKKEI225_weight=0,
    EURONEXT_weight=0,
    SSE_weight=0,
    FTSE_queryset=None,
    SNP500_queryset=None,
    NIKKEI225_queryset=None,
    EURONEXT_queryset=None,
    SSE_queryset=None,
):
    FTSE_total_shares = 0
    SNP500_total_shares = 0
    NIKKEI225_total_shares = 0
    EURONEXT_total_shares = 0
    SSE_total_shares = 0

    FTSE_value = 0
    SNP500_value = 0
    NIKKEI225_value = 0
    EURONEXT_value = 0
    SSE_value = 0

    total_invested = 0

    if FTSE_queryset is not None and len(FTSE_queryset) != 0:
        for monthly_entry in FTSE_queryset:
            FTSE_total_shares += (
                float(amount_monthly) / float(monthly_entry.close)
            ) * float(FTSE_weight)
            FTSE_value = FTSE_total_shares * float(monthly_entry.close)
            total_invested += amount_monthly

    if SNP500_queryset is not None and len(SNP500_queryset) != 0:
        for monthly_entry in SNP500_queryset:
            SNP500_total_shares += (
                float(amount_monthly) / float(monthly_entry.close)
            ) * float(SNP500_weight)
            SNP500_value = SNP500_total_shares * float(monthly_entry.close)

    if NIKKEI225_queryset is not None and len(NIKKEI225_queryset) != 0:
        for monthly_entry in NIKKEI225_queryset:
            NIKKEI225_total_shares += (
                float(amount_monthly) / float(monthly_entry.close)
            ) * float(NIKKEI225_weight)
            NIKKEI225_value = NIKKEI225_total_shares * float(monthly_entry.close)

    if EURONEXT_queryset is not None and len(EURONEXT_queryset) != 0:
        for monthly_entry in EURONEXT_queryset:
            EURONEXT_total_shares += (
                float(amount_monthly) / float(monthly_entry.close)
            ) * float(EURONEXT_weight)
            EURONEXT_value = EURONEXT_total_shares * float(monthly_entry.close)

    if SSE_queryset is not None and len(SSE_queryset) != 0:
        for monthly_entry in SSE_queryset:
            SSE_total_shares += (
                float(amount_monthly) / float(monthly_entry.close)
            ) * float(SSE_weight)
            SSE_value = SSE_total_shares * float(monthly_entry.close)

    return {
        "total_invested": total_invested,
        "end_value": FTSE_value
        + SNP500_value
        + NIKKEI225_value
        + EURONEXT_value
        + SSE_value,
    }


def invest(
    frequency,
    amount,
    start_date,
    end_date,
    FTSE_weight=0,
    SNP500_weight=0,
    NIKKEI225_weight=0,
    EURONEXT_weight=0,
    SSE_weight=0,
):
    FTSE_queryset = FtseData.objects.filter(
        date__range=(start_date, end_date)
    ).order_by("date")

    SNP500_queryset = Snp500Data.objects.filter(
        date__range=(start_date, end_date)
    ).order_by("date")

    NIKKEI225_queryset = Nikkei225Data.objects.filter(
        date__range=(start_date, end_date)
    ).order_by("date")

    EURONEXT_queryset = EuronextData.objects.filter(
        date__range=(start_date, end_date)
    ).order_by("date")

    SSE_queryset = SseData.objects.filter(date__range=(start_date, end_date)).order_by(
        "date"
    )

    if frequency == "daily":
        return invest_daily(
            amount,
            start_date,
            end_date,
            FTSE_weight,
            SNP500_weight,
            NIKKEI225_weight,
            EURONEXT_weight,
            SSE_weight,
            FTSE_queryset,
            SNP500_queryset,
            NIKKEI225_queryset,
            EURONEXT_queryset,
            SSE_queryset,
        )

    elif frequency == "monthly":
        return invest_monthly(
         amount,
            start_date,
            end_date,
            FTSE_weight,
            SNP500_weight,
            NIKKEI225_weight,
            EURONEXT_weight,
            SSE_weight,
            FTSE_queryset,
            SNP500_queryset,
            NIKKEI225_queryset,
            EURONEXT_queryset,
            SSE_queryset,
        )
