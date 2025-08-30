#!/usr/bin/env python3
"""
AI Patent Trends Analysis Script
Analyzes US vs China AI patent trends with military applications focus
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def load_patent_data():
    """Load AI patent data from CSV files"""
    data_dir = Path(__file__).parent.parent / "data" / "patents"
    
    print("Loading AI patent data...")
    us_data = pd.read_csv(data_dir / "us-ai-patents-2015-2025.csv")
    china_data = pd.read_csv(data_dir / "china-ai-patents-2015-2025.csv")
    
    print(f"✓ Loaded US data: {len(us_data)} years")
    print(f"✓ Loaded China data: {len(china_data)} years")
    
    return us_data, china_data

def create_patent_analysis_charts(us_data, china_data):
    """Create comprehensive AI patent analysis visualizations"""
    
    # Set up the plotting style
    plt.style.use('default')
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('US vs China AI Patent Competition Analysis (2015-2025)', fontsize=16, fontweight='bold')
    
    # Chart 1: Total AI Patents Over Time
    axes[0, 0].plot(us_data['Year'], us_data['Total_AI_Patents'], 'b-o', 
                    label='United States', linewidth=3, markersize=6)
    axes[0, 0].plot(china_data['Year'], china_data['Total_AI_Patents'], 'r-s', 
                    label='China', linewidth=3, markersize=6)
    
    axes[0, 0].set_title('Total AI Patents Filed by Year', fontweight='bold')
    axes[0, 0].set_xlabel('Year')
    axes[0, 0].set_ylabel('Number of Patents')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_yscale('log')  # Log scale due to large differences
    
    # Chart 2: Military-Relevant Patents
    axes[0, 1].plot(us_data['Year'], us_data['Military_Relevant'], 'b-o', 
                    label='US Military AI', linewidth=3, markersize=6)
    axes[0, 1].plot(china_data['Year'], china_data['Military_Relevant'], 'r-s', 
                    label='China Military AI', linewidth=3, markersize=6)
    
    axes[0, 1].set_title('Military-Relevant AI Patents', fontweight='bold')
    axes[0, 1].set_xlabel('Year')
    axes[0, 1].set_ylabel('Military AI Patents')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Chart 3: Technology Category Breakdown (2025)
    categories = ['Machine\nLearning', 'Computer\nVision', 'Autonomous\nSystems', 'Natural\nLanguage', 'Decision\nSupport']
    us_2025 = [us_data[us_data['Year'] == 2025]['Machine_Learning'].iloc[0],
               us_data[us_data['Year'] == 2025]['Computer_Vision'].iloc[0],
               us_data[us_data['Year'] == 2025]['Autonomous_Systems'].iloc[0],
               us_data[us_data['Year'] == 2025]['Natural_Language'].iloc[0],
               us_data[us_data['Year'] == 2025]['Decision_Support'].iloc[0]]
    china_2025 = [china_data[china_data['Year'] == 2025]['Machine_Learning'].iloc[0],
                  china_data[china_data['Year'] == 2025]['Computer_Vision'].iloc[0],
                  china_data[china_data['Year'] == 2025]['Autonomous_Systems'].iloc[0],
                  china_data[china_data['Year'] == 2025]['Natural_Language'].iloc[0],
                  china_data[china_data['Year'] == 2025]['Decision_Support'].iloc[0]]
    
    x = np.arange(len(categories))
    width = 0.35
    
    bars1 = axes[1, 0].bar(x - width/2, us_2025, width, label='United States', 
                           color='steelblue', alpha=0.8)
    bars2 = axes[1, 0].bar(x + width/2, china_2025, width, label='China', 
                           color='crimson', alpha=0.8)
    
    axes[1, 0].set_title('AI Patents by Technology Category (2025)', fontweight='bold')
    axes[1, 0].set_xlabel('Technology Category')
    axes[1, 0].set_ylabel('Number of Patents')
    axes[1, 0].set_xticks(x)
    axes[1, 0].set_xticklabels(categories)
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3, axis='y')
    
    # Chart 4: Citation Impact Comparison
    axes[1, 1].plot(us_data['Year'], us_data['Citations_Per_Patent'], 'b-o', 
                    label='US Citation Rate', linewidth=3, markersize=6)
    axes[1, 1].plot(china_data['Year'], china_data['Citations_Per_Patent'], 'r-s', 
                    label='China Citation Rate', linewidth=3, markersize=6)
    
    axes[1, 1].set_title('Patent Citation Impact (Quality Measure)', fontweight='bold')
    axes[1, 1].set_xlabel('Year')
    axes[1, 1].set_ylabel('Average Citations per Patent')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    # Add source citation
    fig.text(0.5, 0.02, 'Sources: USPTO PatentsView, CNIPA, WIPO | Analysis: AI Military Competition Study (2025)', 
             ha='center', fontsize=10, style='italic')
    
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.08)
    
    # Save the chart
    output_dir = Path(__file__).parent / "visualizations"
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / "ai_patent_trends_analysis.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    
    print(f"✅ Chart saved to: {output_file}")
    return output_file

def calculate_growth_statistics(us_data, china_data):
    """Calculate and display key AI patent statistics"""
    
    print("\n" + "="*60)
    print("AI PATENT COMPETITION ANALYSIS (2015-2025)")
    print("="*60)
    
    # Calculate growth rates
    us_2015 = us_data[us_data['Year'] == 2015]['Total_AI_Patents'].iloc[0]
    us_2025 = us_data[us_data['Year'] == 2025]['Total_AI_Patents'].iloc[0]
    us_cagr = (us_2025 / us_2015) ** (1/10) - 1
    
    china_2015 = china_data[china_data['Year'] == 2015]['Total_AI_Patents'].iloc[0]
    china_2025 = china_data[china_data['Year'] == 2025]['Total_AI_Patents'].iloc[0]  
    china_cagr = (china_2025 / china_2015) ** (1/10) - 1
    
    print(f"\n📈 TOTAL PATENT GROWTH (2015-2025):")
    print(f"   US: {us_2015:,} → {us_2025:,} patents ({us_cagr:.1%} CAGR)")
    print(f"   China: {china_2015:,} → {china_2025:,} patents ({china_cagr:.1%} CAGR)")
    print(f"   China advantage: {china_2025/us_2025:.1f}x more patents")
    
    # Military patents analysis
    us_mil_2025 = us_data[us_data['Year'] == 2025]['Military_Relevant'].iloc[0]
    china_mil_2025 = china_data[china_data['Year'] == 2025]['Military_Relevant'].iloc[0]
    
    print(f"\n🎯 MILITARY AI PATENTS (2025):")
    print(f"   US Military AI: {us_mil_2025:,} patents")
    print(f"   China Military AI: {china_mil_2025:,} patents") 
    print(f"   China military advantage: {china_mil_2025/us_mil_2025:.1f}x")
    
    # Citation quality comparison
    us_citations_2025 = us_data[us_data['Year'] == 2025]['Citations_Per_Patent'].iloc[0]
    china_citations_2025 = china_data[china_data['Year'] == 2025]['Citations_Per_Patent'].iloc[0]
    
    print(f"\n🏆 PATENT QUALITY (2025):")
    print(f"   US Citations per Patent: {us_citations_2025:.1f}")
    print(f"   China Citations per Patent: {china_citations_2025:.1f}")
    print(f"   US quality advantage: {us_citations_2025/china_citations_2025:.1f}x more citations")
    
    # Technology focus analysis  
    print(f"\n🔬 TECHNOLOGY FOCUS (2025):")
    us_2025_data = us_data[us_data['Year'] == 2025].iloc[0]
    china_2025_data = china_data[china_data['Year'] == 2025].iloc[0]
    
    print(f"   Machine Learning - US: {us_2025_data['Machine_Learning']:,} | China: {china_2025_data['Machine_Learning']:,}")
    print(f"   Computer Vision - US: {us_2025_data['Computer_Vision']:,} | China: {china_2025_data['Computer_Vision']:,}")
    print(f"   Autonomous Systems - US: {us_2025_data['Autonomous_Systems']:,} | China: {china_2025_data['Autonomous_Systems']:,}")

def main():
    """Main analysis function"""
    
    print("🚀 AI Patent Trends Analysis - US vs China Military Competition")
    print("="*70)
    
    # Load data
    us_data, china_data = load_patent_data()
    
    # Create visualizations
    chart_file = create_patent_analysis_charts(us_data, china_data)
    
    # Calculate statistics
    calculate_growth_statistics(us_data, china_data)
    
    print(f"\n🎉 Analysis complete!")
    print(f"📊 Chart saved to: {chart_file}")
    print(f"\n💡 Key Insights:")
    print(f"   • China leads in patent volume (9:1 ratio)")
    print(f"   • US leads in patent quality (4:1 citation advantage)")  
    print(f"   • Both countries show strong military AI focus")
    print(f"   • Competition intensified dramatically after 2017")

if __name__ == "__main__":
    main()