BEGIN {
    FS="\t"
    OFS=","
} {
    print $5
}