void align() {

    ifstream infile("posX.txt");

    TGraphErrors *g1 = new TGraphErrors();
    TH1F *f1 = new TH1F("th1","",10,0.10,0.17);
    g1->SetName("g1");
    g1->SetTitle(";relative delay, t_{delay} [ns]; relative intime-efficiency [%]");

    //gStyle->SetOptFit(1011);

    Int_t pt=0;
    Double_t x=0.;
    char delim;
    //infile >> e_vs >> e_vc;

    while (1) {
            if(!infile.good()) break;
            infile >> x;
            g1->SetPoint(pt, pt, x);
            f1->Fill(x);
   //         g1->SetPointError(pt, 0, 0.3);
        pt++;
    }
    infile.close();
    
    g1->SetMarkerStyle(kFullCircle);
    g1->SetMarkerColor(kBlue+1);
    //g1->GetXaxis()->SetRangeUser(0,30);
    //g1->Draw("ap");
    f1->Draw("");

}
