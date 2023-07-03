BEGIN {
    FS="\t"
    OFS=","
}
{
    print $6, " "$7, " "$8" - "$9
}