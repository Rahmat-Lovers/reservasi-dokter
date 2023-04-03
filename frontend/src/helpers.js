function getDistanceYear(date2) {
    // Buat objek Date dari tanggal pertama dan kedua
    var date1 = new Date();

    // Hitung selisih waktu antara dua tanggal dalam milidetik
    var timeDiff = Math.abs(date2.getTime() - date1.getTime());

    // Hitung jumlah hari dalam selisih waktu
    var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));

    return Math.floor(diffDays / 365)
}

export {
    getDistanceYear
}