#include<bits/stdc++.h>
using namespace std;
map<string,int> dicc;
bool x(char r)
{
	if(r>='a'&&r<='z')return true;
	return false;
}
int ggg[30];int tot=27782;
void predeal(string s)
{
	int brac[26];
	memset(brac,0,sizeof(brac));
	brac[s[0]-'a']=1;
	brac[s[1]-'a']=1;
	brac[s[2]-'a']=1;
	brac[s[3]-'a']=1;
	brac[s[4]-'a']=1;
	for(int i=0;i<=25;i++)
		ggg[i]+=brac[i];
}
int counting[26][5];
double sideal(string anss,string guss){
	//cout<<guss<<endl;
	if(anss==guss)return 0;
	int situ[6];
	memset(situ,0,sizeof(situ));
	int brac[26];
	brac[anss[0]-'a']++;
	brac[anss[1]-'a']++;
	brac[anss[2]-'a']++;
	brac[anss[3]-'a']++;
	brac[anss[4]-'a']++;
	situ[0]=(anss[0]==guss[0]);
	situ[1]=(anss[1]==guss[1]);
	situ[2]=(anss[2]==guss[2]);
	situ[3]=(anss[3]==guss[3]);
	situ[4]=(anss[4]==guss[4]);
	situ[0]=(!situ[0]&&brac[guss[0]-'a'])?2:situ[0];
	situ[1]=(!situ[1]&&brac[guss[1]-'a'])?2:situ[1];
	situ[2]=(!situ[2]&&brac[guss[2]-'a'])?2:situ[2];
	situ[3]=(!situ[3]&&brac[guss[3]-'a'])?2:situ[3];
	situ[4]=(!situ[4]&&brac[guss[4]-'a'])?2:situ[4];
	//cout<<situ[0]<<situ[1]<<situ[2]<<situ[3]<<situ[4]<<endl;
	double vv=0;
	for(int i=0;i<=4;i++)
		//cout<<i<<" "<<counting[guss[i]-'a'][i]<<" "<<ggg[guss[i]-'a']<<" "<<tot-ggg[guss[i]-'a']-counting[guss[i]-'a'][i]<<endl,
		vv+=log2((anss[i]==guss[i])?counting[guss[i]-'a'][i]:
	      (~situ[i])?(tot-ggg[guss[i]-'a']):(ggg[guss[i]-'a']-counting[guss[i]-'a'][i]))-log2(tot);
	//cout<<vv<<endl;
	vv+=log2(tot);
	if(vv<-20)
	{
		cout<<guss<<endl;
		for(int i=0;i<=4;i++)
		cout<<i<<" "<<counting[guss[i]-'a'][i]<<" "<<ggg[guss[i]-'a']<<" "<<tot-ggg[guss[i]-'a']-counting[guss[i]-'a'][i]<<endl;
		cout<<vv<<endl;
	}
	assert (vv>-20);
	
	return vv;

}

int main()
{
	string s1,s2;
	freopen("en_full.txt","r",stdin);
	freopen("result1.txt","w",stdout);
	int i,pinlv;
	for(i=1;i<=1656996;i++)
	//cin>>s1>>s2,dicc[s1]=s2;
	{
		cin>>s1>>s2;
		stringstream ss;
		int xxx;
		ss << s2;
		ss >> xxx;
		if(xxx<10)break;
		if(s1.length()==5)
		{
			//cout<<s1[0]<<x(s1[0])<<s1[1]<<x(s1[1])<<s1[2]<<x(s1[2])<<s1[3]<<x(s1[3])<<"     ";
			if(x(s1[0])&&x(s1[1])&&x(s1[2])&&x(s1[3])&&x(s1[4]))
			{
				//cout<<s1<<endl;
				dicc[s1]=xxx;pinlv+=xxx;
				predeal(s1);
				counting[s1[0]-'a'][0]++;
				counting[s1[1]-'a'][1]++;
				counting[s1[2]-'a'][2]++;
				counting[s1[3]-'a'][3]++;
				counting[s1[4]-'a'][4]++;
			}
		}
	}
	for(;i<=1656996;i++)
	//cin>>s1>>s2,dicc[s1]=s2;
	{
		cin>>s1>>s2;
		if(s1=="jjonah")break;
	}
		
	
	
	for(int ww=1;ww<=359;ww++)
	{
		string s;
		cin>>s;
		//cout<<ww<<" "<<s<<endl;
		double ans=0;
		for(auto it=dicc.begin();it!=dicc.end();it++)
			ans+=1.0*it->second*sideal(s,it->first)/tot;
		ans/=1.0*tot;
		//if(ans<1)cout<<s<<" ";
		//if(ans>1.2)cout<<s<<"  ";
		cout<<ans<<endl;
	}
	
	return 0;
}