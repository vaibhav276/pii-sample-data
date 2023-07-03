BEGIN {
    FS="\t"
    OFS=","
}
{
    print $2
}
