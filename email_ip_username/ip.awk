BEGIN {
    FS=","
    OFS=","
}
{
    print $4
}