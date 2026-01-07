<?php

namespace Database\Seeders;

use App\Models\Work;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class WorksSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $works = [
            // ETV特集
            [
                'title' => '断らない ある市役所の実践',
                'broadcast_date' => '2023-09-01',
                'category' => 'etv_special',
                'description' => '神奈川県座間市生活援護課は、「誰も断らない、見捨てない」をモットーに生活困窮者支援に取り組んでいる。迷いながら奮闘する職員たちの、役所内外の日々に密着。',
                'link_url' => null,
                'display_order' => 1,
                'is_published' => true,
            ],
            [
                'title' => '迷える女性たちの家',
                'broadcast_date' => '2022-06-01',
                'category' => 'etv_special',
                'description' => 'とある街の一角にある、行き場を失った女性たちのためのシェルター。「女性の居場所Jikka（実家）」に駆け込み、暮らしを立て直そうとする女性たちの日々に密着。',
                'link_url' => 'https://www.nhk.or.jp/',
                'display_order' => 2,
                'is_published' => true,
            ],
            [
                'title' => 'この国で生きてゆく ～大阪 外国ルーツの子どもたち',
                'broadcast_date' => '2021-05-01',
                'category' => 'etv_special',
                'description' => '大阪ミナミの歓楽街。その一角に、外国ルーツの子どもたちに勉強を教える夜間教室がある。コロナ禍のなか、通ってくる子どもたちとその家族を1年に渡って見つめた。',
                'link_url' => 'https://www.nhk.or.jp/',
                'display_order' => 3,
                'is_published' => true,
            ],
            // 4K特集
            [
                'title' => 'すべてのものが幸福にしかなれない處 ～京都・五条坂 河井寬次郎家の人々',
                'broadcast_date' => '2023-05-01',
                'category' => '4k_special',
                'description' => '日本を代表する陶工、河井寛次郎(1890-1966)。焼き物だけでなく、胸に響く多くの「言葉」を遺した。祖父の言葉を胸に、人生をよりよく生きようとした家族の物語。',
                'link_url' => 'https://www.nhk.or.jp/archives/',
                'display_order' => 4,
                'is_published' => true,
            ],
            // 日曜美術館
            [
                'title' => 'だからあんな不思議な絵を 〜夭折の画家・有元利夫と家族〜',
                'broadcast_date' => '2025-09-01',
                'category' => 'nichiyo_bijutsu',
                'description' => '日本の高度成長期に、幻想に満ちた絵画世界で一世を風靡した画家・有元利夫。38歳の若さで亡くなった後、日本画家だった妻と生まれて間もない息子が遺された。',
                'link_url' => null,
                'display_order' => 5,
                'is_published' => true,
            ],
            [
                'title' => '人生で美しいとは何か 彫刻家・舟越保武と子どもたち',
                'broadcast_date' => '2025-01-01',
                'category' => 'nichiyo_bijutsu',
                'description' => '日本を代表する彫刻家、舟越保武（1912-2002）。末盛千枝子、舟越桂、舟越直木、舟越カンナ･･･。作品を通して父と対話を続ける子どもたちの人生。',
                'link_url' => null,
                'display_order' => 6,
                'is_published' => true,
            ],
            [
                'title' => '美は喜び 河井寬次郎 住める哲学',
                'broadcast_date' => '2024-01-01',
                'category' => 'nichiyo_bijutsu',
                'description' => '京都・五条坂にたたずむ河井寬次郎の旧居。ここは寛次郎自ら設計した建物で、孫たちが記念館として公開。「暮らし」と「美」の一体を目指した寬次郎の哲学に迫る。',
                'link_url' => 'https://www.nhk.or.jp/',
                'display_order' => 7,
                'is_published' => true,
            ],
            // その他
            [
                'title' => '知っていますか？ ハンセン病問題',
                'broadcast_date' => '2021-06-01',
                'category' => 'other',
                'description' => 'ハンセン病について、医学、歴史、現在の課題まで、基本的な知識を、山内きみ江さんの語りを軸に、わかりやすくまとめたもの。',
                'link_url' => null,
                'display_order' => 8,
                'is_published' => true,
            ],
        ];

        foreach ($works as $work) {
            Work::create($work);
        }
    }
}
