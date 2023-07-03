BEGIN {
    FS="\t"
    OFS=","
}
{
    print $1
}