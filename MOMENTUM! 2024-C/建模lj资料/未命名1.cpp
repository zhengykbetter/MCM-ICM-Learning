#include<bits/stdc++.h>
using namespace std;
int tot[50];//0 1 2 3 4 5 6
int trans[50][50]={0};
int mm(string s){
	int x=(s[0]-'0')*7+(s[2]-'0');
	assert(x<=49);
	return x;
}
string sss(int x){
	string s;
	s.push_back(x/7+'0');
	s.push_back(',');
	s.push_back(x%7+'0');
	return s;
}
int main()
{
	freopen("re.txt","w",stdout);
	string strrem=",,,";
	for(int i=1;i<=1188;i++)//7284
	{
		string xx;
		cin>>xx;
		//if(xx!=strrem)cout<<xx;
		//strrem=xx;
		
		if(strrem[0]==strrem[2])
		{
			strrem=xx;
			continue;
		}
		tot[mm(strrem)]++;
		trans[mm(strrem)][mm(xx)]++;
		//assert(trans[mm(strrem)][mm(xx)])
		strrem=xx;
		
	}
	//cout<<finished; 
	
	for(int i=0;i<=49;i++)
	{
		if(tot[i]==0)continue;
		cout<<sss(i)<<" tot: "<<tot[i]<<endl;
		for(int j=0;j<=49;j++)
		{
			if(trans[i][j]==0)continue;
			cout<<"  "<<sss(j)<<":"<<trans[i][j]<<endl;
		}

	}
	

	return 0;
}
