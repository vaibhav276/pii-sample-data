BEGIN {
    FS="\t"
    OFS=","
} {
    print $7
}
