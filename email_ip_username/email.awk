BEGIN {
    FS=","
    OFS=","
}
{
    print $3
}