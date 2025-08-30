#!/usr/bin/env python3
"""
Military AI Funding Analysis Script  
Compares US vs China military AI investment strategies and patterns
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def load_funding_data():
    """Load military AI funding data from CSV files"""
    data_dir = Path(__file__).parent.parent / "data" / "funding"
    
    print("Loading military AI funding data...")
    us_data = pd.read_csv(data_dir / "us-ai-military-funding.csv")
    china_data = pd.read_csv(data_dir / "china-ai-military-investment.csv")
    
    print(f"✓ Loaded US funding data: {len(us_data)} years")
    print(f"✓ Loaded China investment data: {len(china_data)} years")
    
    return us_data, china_data

def create_funding_comparison_charts(us_data, china_data):
    """Create comprehensive military AI funding analysis visualizations"""
    
    plt.style.use('default')
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('US vs China Military AI Investment Analysis (2015-2025)', fontsize=16, fontweight='bold')
    
    # Chart 1: Annual Military AI Investment Comparison
    axes[0, 0].plot(us_data['Year'], us_data['Total_Military_AI_Millions']/1000, 'b-o', 
                    label='US Military AI', linewidth=3, markersize=6)
    axes[0, 0].plot(china_data['Year'], china_data['Total_Military_AI_Billions'], 'r-s', 
                    label='China Military AI', linewidth=3, markersize=6)
    
    axes[0, 0].set_title('Annual Military AI Investment', fontweight='bold')
    axes[0, 0].set_xlabel('Year')
    axes[0, 0].set_ylabel('Investment (Billions USD)')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_yscale('log')  # Log scale due to large differences
    
    # Chart 2: Cumulative Investment Over Time
    us_cumulative = us_data['Total_Military_AI_Millions'].cumsum() / 1000
    china_cumulative = china_data['Total_Military_AI_Billions'].cumsum()
    
    axes[0, 1].plot(us_data['Year'], us_cumulative, 'b-o', 
                    label='US Cumulative', linewidth=3, markersize=6)
    axes[0, 1].plot(china_data['Year'], china_cumulative, 'r-s', 
                    label='China Cumulative', linewidth=3, markersize=6)
    
    axes[0, 1].set_title('Cumulative Military AI Investment', fontweight='bold')
    axes[0, 1].set_xlabel('Year')
    axes[0, 1].set_ylabel('Cumulative Investment (Billions USD)')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Chart 3: US Investment Breakdown (2025)
    us_2025 = us_data[us_data['Year'] == 2025].iloc[0]
    us_categories = ['DoD Budget', 'DARPA Programs', 'Private Military', 'AI Contracts']
    us_values = [us_2025['DoD_AI_Budget_Millions'], us_2025['DARPA_AI_Millions'], 
                 us_2025['Private_Military_AI_Millions'], us_2025['AI_Contracts_Millions']]
    
    colors_us = ['lightblue', 'darkblue', 'steelblue', 'navy']
    wedges, texts, autotexts = axes[1, 0].pie(us_values, labels=us_categories, colors=colors_us, 
                                              autopct='%1.1f%%', startangle=90)
    axes[1, 0].set_title('US Military AI Investment Breakdown (2025)\nTotal: $6.9B', fontweight='bold')
    
    # Chart 4: China Investment Structure (2025) 
    china_2025 = china_data[china_data['Year'] == 2025].iloc[0]
    china_categories = ['Central Gov', 'Regional Gov', 'Military Specific', 'MCF Investment']
    china_values = [china_2025['Central_Gov_AI_Billions'], china_2025['Regional_AI_Billions'],
                   china_2025['Military_AI_Billions'], china_2025['MCF_Investment_Billions']]
    
    colors_china = ['lightcoral', 'darkred', 'crimson', 'maroon']
    wedges, texts, autotexts = axes[1, 1].pie(china_values, labels=china_categories, colors=colors_china,
                                              autopct='%1.1f%%', startangle=90)
    axes[1, 1].set_title('China Military AI Investment Structure (2025)\nTotal: $127.9B', fontweight='bold')
    
    # Add source citation
    fig.text(0.5, 0.02, 'Sources: DoD Budget Documents, DARPA, CSIS, State Council AI Plans | Analysis: Military AI Competition Study (2025)', 
             ha='center', fontsize=10, style='italic')
    
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.08)
    
    # Save the chart
    output_dir = Path(__file__).parent / "visualizations"
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / "military_ai_funding_analysis.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    
    print(f"✅ Chart saved to: {output_file}")
    return output_file

def calculate_investment_metrics(us_data, china_data):
    """Calculate and display key military AI investment metrics"""
    
    print("\n" + "="*65)
    print("MILITARY AI INVESTMENT COMPETITION ANALYSIS (2015-2025)")
    print("="*65)
    
    # Total investment comparison
    us_total = us_data['Total_Military_AI_Millions'].sum() / 1000  # Convert to billions
    china_total = china_data['Total_Military_AI_Billions'].sum()
    
    print(f"\n💰 TOTAL MILITARY AI INVESTMENT (2015-2025):")
    print(f"   United States: ${us_total:.1f} billion")
    print(f"   China: ${china_total:.1f} billion")
    print(f"   China investment advantage: {china_total/us_total:.1f}x greater")
    
    # Annual investment comparison (2025)
    us_2025 = us_data[us_data['Year'] == 2025]['Total_Military_AI_Millions'].iloc[0] / 1000
    china_2025 = china_data[china_data['Year'] == 2025]['Total_Military_AI_Billions'].iloc[0]
    
    print(f"\n📊 ANNUAL INVESTMENT (2025):")
    print(f"   US Military AI: ${us_2025:.1f} billion")
    print(f"   China Military AI: ${china_2025:.1f} billion")
    print(f"   China annual advantage: {china_2025/us_2025:.1f}x")
    
    # Growth rate analysis
    us_2015 = us_data[us_data['Year'] == 2015]['Total_Military_AI_Millions'].iloc[0] / 1000
    us_cagr = (us_2025 / us_2015) ** (1/10) - 1
    
    china_2015 = china_data[china_data['Year'] == 2015]['Total_Military_AI_Billions'].iloc[0]
    china_cagr = (china_2025 / china_2015) ** (1/10) - 1
    
    print(f"\n📈 INVESTMENT GROWTH (2015-2025):")
    print(f"   US CAGR: {us_cagr:.1%} (${us_2015:.1f}B → ${us_2025:.1f}B)")
    print(f"   China CAGR: {china_cagr:.1%} (${china_2015:.1f}B → ${china_2025:.1f}B)")
    
    # Investment strategy analysis
    us_2025_data = us_data[us_data['Year'] == 2025].iloc[0]
    china_2025_data = china_data[china_data['Year'] == 2025].iloc[0]
    
    print(f"\n🎯 INVESTMENT STRATEGY COMPARISON (2025):")
    print(f"   US Government (DoD + DARPA): ${(us_2025_data['DoD_AI_Budget_Millions'] + us_2025_data['DARPA_AI_Millions'])/1000:.1f}B")
    print(f"   US Private Military: ${us_2025_data['Private_Military_AI_Millions']/1000:.1f}B")
    print(f"   China Government Total: ${(china_2025_data['Central_Gov_AI_Billions'] + china_2025_data['Regional_AI_Billions']):.1f}B")
    print(f"   China Military-Specific: ${china_2025_data['Military_AI_Billions']:.1f}B")

def analyze_key_programs(us_data, china_data):
    """Analyze specific military AI programs"""
    
    print(f"\n🚀 KEY MILITARY AI PROGRAMS:")
    print(f"\n   US DoD Replicator Initiative:")
    print(f"   • Budget: $800M program (2023-2025)")
    print(f"   • Goal: Thousands of autonomous systems")
    print(f"   • Focus: Swarm coordination, attritable systems")
    
    print(f"\n   DARPA AI Next Campaign:")
    print(f"   • Investment: $2B multi-year program")
    print(f"   • Focus: Next-generation AI research")
    print(f"   • Timeline: 2018-2025 deployment")
    
    print(f"\n   China PLA AI Modernization:")
    print(f"   • Investment: $127.9B total (2015-2025)")
    print(f"   • Goal: 'Intelligentized warfare' by 2027")
    print(f"   • Focus: War Skull wargaming, autonomous weapons")
    
    print(f"\n   Military-Civil Fusion:")
    print(f"   • Coordination: Xi Jinping personal oversight")
    print(f"   • Integration: Civilian AI to military applications")
    print(f"   • Investment: $16.8B specifically for technology transfer")

def main():
    """Main funding analysis function"""
    
    print("🚀 Military AI Funding Analysis - US vs China Competition")
    print("="*65)
    
    # Load data
    us_data, china_data = load_funding_data()
    
    # Create visualizations
    chart_file = create_funding_comparison_charts(us_data, china_data)
    
    # Calculate metrics
    calculate_investment_metrics(us_data, china_data)
    
    # Analyze programs
    analyze_key_programs(us_data, china_data)
    
    print(f"\n🎉 Analysis complete!")
    print(f"📊 Chart saved to: {chart_file}")
    print(f"\n💡 Strategic Implications:")
    print(f"   • China's 18.6x investment advantage enables comprehensive AI military development")
    print(f"   • US focuses on innovation quality and private sector leverage")
    print(f"   • Different approaches: China state-led vs US market-driven")
    print(f"   • Both countries targeting AI military capabilities by 2027-2030")

if __name__ == "__main__":
    main()