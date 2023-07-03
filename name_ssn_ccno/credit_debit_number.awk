BEGIN {
    FS="\t"
    OFS=","
}
{
    print $3
}
